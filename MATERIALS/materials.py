from abaqus import mdb
from abaqusConstants import *


def ElasticMaterial(modelName, name, data, sectionLength=1.):
    m = mdb.models[modelName]
    mat = m.Material(name=name)
    sect_name = name + '_Section'
    sect = m.HomogeneousSolidSection(name=sect_name,
                                     material=name,
                                     thickness=sectionLength)
    if data.get('density') is not None:
        mat.Density(table=((data.get('density'),),))

    if data.get('elastic') is not None:
        mat.Elastic(table=(data.get('elastic'),))

    if data.get('conductivity') is not None:
        mat.Conductivity(table=((data.get('conductivity'),),))

    if data.get('specific_heat') is not None:
        mat.SpecificHeat(table=((data.get('specific_heat'),),))

    if data.get('expansion') is not None:
        mat.Expansion(table=((data.get('expansion'),),))
    subroutine = None
    return mat, sect, subroutine


def vonMisesMaterial(modelName, name, data, sectionLength=1.):
    mat, sect, subroutine = ElasticMaterial(
        modelName, name, data, sectionLength)
    if data.get("stress_strain_curve") is not None:
        mat.Plastic(table=data["stress_strain_curve"])
    return mat, sect, subroutine


def MohrCoulombMaterial(modelName, name, data, sectionLength=1.):
    mat, sect, subroutine = ElasticMaterial(
        modelName, name, data, sectionLength)
    phi = data.get("friction_angle")
    dilat = data.get("dilatancy_angle")
    c = data.get("cohesion")
    labData = data.get("lab_data")
    if None in (phi, c, labData):
        raise ValueError(
            "friction_angle, dilatancy_angle, cohesion, and lab_data must be provided for Mohr-Coulomb material.")
        return
    if dilat is None:
        dilat = 0.0
    mat.MohrCoulombPlasticity(table=((phi, dilat), ))
    mat.mohrCoulombPlasticity.MohrCoulombHardening(table=labData)
    mat.mohrCoulombPlasticity.TensionCutOff(temperatureDependency=OFF, dependencies=0,
                                            table=((c, 0.0), ))

    return mat, sect, subroutine

    # mat.Creep(law=USER, table=())


def DoublePowerCreepMaterial(modelName, name, data, sectionLength=1.):
    mat, sect, subroutine = ElasticMaterial(
        modelName, name, data, sectionLength)
    try:
        dp_data = data.get("creep_parameters", {})
        A1 = dp_data["A1"]
        A2 = dp_data["A2"]
        B1 = dp_data["B1"]
        B2 = dp_data["B2"]
        C1 = dp_data["C1"]
        C2 = dp_data["C2"]
        ref_stress = dp_data["reference_stress"]
        mat.Creep(law=DOUBLE_POWER,
                  table=((A1, B1, C1, A2, B2, C2, ref_stress),))
    except:
        raise ValueError(
            "double_power_creep_data with A1, A2, B1, B2, C1, C2, and reference_stress must be provided for Double Power Creep material.")
    return mat, sect, subroutine


def DoubleMechanismCreepMaterial(modelName, name, data, sectionLength=1.):
    mat, sect, subroutine = ElasticMaterial(
        modelName, name, data, sectionLength)
    mat.Creep(law=USER, table=())
    subroutine = {"CREEP": " my fortran subroutine "}
    return mat, sect, subroutine


def CreateMaterial(modelName, name, data, sectionLength=1.):
    behavior = data.get("behavior")
    mapping = {
        "Elastic": ElasticMaterial,
        "vonMises": vonMisesMaterial,
        "MohrCoulomb": MohrCoulombMaterial,
        "DoublePowerCreep": DoublePowerCreepMaterial,
        "DoubleMechanismCreep": DoubleMechanismCreepMaterial,
    }
    create_func = mapping.get(behavior)
    if create_func is not None:
        return create_func(modelName, name, data, sectionLength)
    else:
        raise ValueError("Behavior '%s' not recognized." % behavior)


def Assign_Section(modelName, partName, sectionName, setName=None, isSolid=True):
    model = mdb.models[modelName]
    # Only allow assignments for specific parts (material examples)
    allowed_parts = ("PIPE", "FLUID")
    if partName not in allowed_parts:
        print("Skipping section assignment for '%s' (not in allowed parts: %s)" % (partName, allowed_parts))
        return
    if partName not in model.parts:
        raise ValueError("Part '%s' not found in model '%s'." %
                         (partName, modelName))
    part = model.parts[partName]

    if sectionName not in model.sections:
        raise ValueError("Section '%s' not found in model '%s'. Available sections are: %s" % (
            sectionName, modelName, list(model.sections.keys())))

    if setName is None:
        setName = partName + '_Set'
    if setName in part.sets:
        region = part.sets[setName]
    else:
        if part.space in (TWO_D_PLANAR, AXISYMMETRIC):
            region = part.Set(name=setName, faces=part.faces[:])
        elif part.space == THREE_D:
            region = part.Set(name=setName, cells=part.cells[:])
        # if isSolid is True:
        #     region = part.Set(name=setName, cells=part.cells[:])
        # elif isSolid is False:
        else:
            raise ValueError("No valid entities to assign section in %s" % partName)

    part.SectionAssignment(region=region,
                           sectionName=sectionName,
                           offset=0.0,
                           offsetType=MIDDLE_SURFACE,
                           offsetField='',
                           thicknessAssignment=FROM_SECTION)
    
# def AssignRockByDepth(modelName, partName, top_depth, base_depth, layer_depths, materials_order=None):
#     """
#     Create sets for each partitioned layer (using depths) and assign rock material
#     sections to them. The function expects the part already partitioned by
#     horizontal planes at the values in `layer_depths` (see `PartitionLayersByDepth`).

#     Parameters
#     - modelName: name of the Abaqus model
#     - partName: name of the Part (e.g. 'ROCK')
#     - top_depth: top depth (numeric)
#     - base_depth: base depth (numeric)
#     - layer_depths: list of intermediate depths (numeric)
#     - materials_order: list of material names (e.g. ['SHALE','SANDSTONE','HALITE']).
#       If shorter than number of layers it will be cycled.

#     Example:
#         AssignRockByDepth('MyFirstModel', 'ROCK', 3200, 4250, [3300,3600,4000],
#                           materials_order=['SHALE','SANDSTONE','HALITE'])
#     """
#     model = mdb.models[modelName]
#     if partName not in model.parts:
#         raise ValueError("Part '%s' not found in model '%s'." % (partName, modelName))
#     p = model.parts[partName]

#     # build full ordered depth list from top -> base
#     mids = sorted(layer_depths or [])
#     depths = [top_depth] + mids + [base_depth]

#     if materials_order is None:
#         materials_order = ['SHALE', 'SANDSTONE', 'HALITE']

#     num_layers = len(depths) - 1

#     for i in range(num_layers):
#         layer_top = depths[i]
#         layer_bottom = depths[i + 1]
#         # name the set for clarity
#         set_name = '%s_Layer_%d_%d_%d' % (partName, i + 1, int(layer_top), int(layer_bottom))

#         # collect faces whose representative point lies between the two depths
#         faces_for_layer = []
#         for f in p.faces[:]:
#             # face.pointOn is a representative point (x,y,z)
#             try:
#                 y = f.pointOn[1]
#             except Exception:
#                 # fallback: skip face if we can't get pointOn
#                 continue
#             # model uses negative Y for depths (partition used -depth)
#             if (-layer_bottom) <= y <= (-layer_top):
#                 faces_for_layer.append(f)

#         if not faces_for_layer:
#             print("Warning: no faces found for layer %d (%s to %s)" % (i + 1, layer_top, layer_bottom))
#             continue

#         # create or replace set
#         if set_name in p.sets:
#             region = p.sets[set_name]
#         else:
#             region = p.Set(name=set_name, faces=faces_for_layer)

#         # pick material for this layer (cycle through materials_order)
#         mat_name = materials_order[i % len(materials_order)]
#         section_name = '%s_Section' % mat_name
#         if section_name not in model.sections:
#             print("Warning: section '%s' not found in model; skipping assignment for %s" % (section_name, set_name))
#             continue

#         p.SectionAssignment(
#             region=region,
#             sectionName=section_name,
#             offset=0.0,
#             offsetType=MIDDLE_SURFACE,
#             offsetField='',
#             thicknessAssignment=FROM_SECTION
#         )
#         print('Assigned %s to %s (depth %s-%s)' % (mat_name, set_name, layer_top, layer_bottom))
