# -*- coding: utf-8 -*-
from abaqus import *
from abaqusConstants import *
import displayGroupMdbToolset as dgm


def Pipe(name_model, name_part, inner_radius, base_depth, top_depth, thickness):

    # depth = base_depth - top_depth
    # Criancao do Sketch - Geometria do Revestimento
    sketch_name = '__profile__' + name_part
    s = mdb.models[name_model].ConstrainedSketch(
        name=sketch_name, sheetSize=10000.0)
    s.sketchOptions.setValues(viewStyle=AXISYM)
    s.setPrimaryObject(option=STANDALONE)

    # Criacao da Linha de Axisimetria
    axis = s.ConstructionLine(point1=(0.0, -10000.0), point2=(0.0, 10000.0))
    s.FixedConstraint(entity=axis)

    # Construcao da Geometria do Revestimento
    s.rectangle(point1=(inner_radius, -(top_depth)),
                point2=(inner_radius + thickness, -(base_depth)))

    p = mdb.models[name_model].Part(
        name=name_part, dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    return p


def Fluid(name_model, name_part, inner_radius, base_depth, top_depth, thickness):

    # depth = base_depth - top_depth
    # Criacao do Sketch - Geometria do Revestimento
    sketch_name = '__profile__' + name_part
    s1 = mdb.models[name_model].ConstrainedSketch(
        name=sketch_name, sheetSize=1000.0)
    s1.sketchOptions.setValues(viewStyle=AXISYM)
    s1.setPrimaryObject(option=STANDALONE)

    # Criacao da Linha de Axisimetria
    axis = s1.ConstructionLine(point1=(0.0, -10000.0), point2=(0.0, 10000.0))
    s1.FixedConstraint(entity=axis)

    # Construcao da Geometria do Fluido/Anular
    s1.rectangle(point1=(inner_radius, -(top_depth)),
                 point2=(inner_radius + thickness, -(base_depth)))

    p = mdb.models[name_model].Part(
        name=name_part, dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s1)
    s1.unsetPrimaryObject()
    return p


def Rock(name_model, name_part, inner_radius, base_depth, top_depth, thickness):

    # depth = base_depth - top_depth
    # Criacao do Sketch - Geometria da Rocha
    sketch_name = '__profile__' + name_part
    s2 = mdb.models[name_model].ConstrainedSketch(
        name=sketch_name, sheetSize=1000.0)
    s2.sketchOptions.setValues(viewStyle=AXISYM)
    s2.setPrimaryObject(option=STANDALONE)

    # Criacao da Linha de Axisimetria
    axis = s2.ConstructionLine(point1=(0.0, -10000.0), point2=(0.0, 10000.0))
    s2.FixedConstraint(entity=axis)

    # Construcao da Geometria da Rocha
    s2.rectangle(point1=(inner_radius, -(top_depth)),
                 point2=(inner_radius + thickness, -(base_depth)))

    p = mdb.models[name_model].Part(
        name=name_part, dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s2)
    s2.unsetPrimaryObject()
    # Criacao dos Reference Points nas profundidades de topo
    s2.Line(point1=(0, top_depth), point2=(1000, top_depth))
    rp_top = p.ReferencePoint(point=(0.0, -(top_depth), 0.0))
    p.Set(name='RP_TOP_%s' % top_depth, referencePoints=(
        p.referencePoints[rp_top.id], ))
    # Criacao dos Reference Points nas profundidades de base
    s2.Line(point1=(0, base_depth), point2=(1000, base_depth))
    # rp_base = p.ReferencePoint(point=(0.0, -(base_depth), 0.0))
    # p.Set(name='RP_BASE_%s' % base_depth, referencePoints=(p.referencePoints[rp_base.id], ))

    return p


def CreateGeometry(name_model, name, data):
    print("Creating Geometry: ", name)

    geometry = {
        "ROCK": Rock,
        "FLUID": Fluid,
        "PIPE": Pipe
    }

    geom_func = geometry.get(name)
    if geom_func is not None:
        return geom_func(name_model,
                         name,
                         data["inner_radius"],
                         data["base_depth"],
                         data["top_depth"],
                         data["thickness"]
                         )
    else:
        raise ValueError("Geometry type '%s' is not recognized." % name)


def PartitionLayersByDepth(modelName, part_name, layer_depths):
    model = mdb.models[modelName]
    p = model.parts[part_name]
    datum_ids = []

    # 1. Criacao dos Planos Datum
    for depth in layer_depths:
        y_coord = -float(depth)
        dp = p.DatumPlaneByPrincipalPlane(
            principalPlane=XZPLANE, offset=y_coord)
        datum_ids.append(dp.id)

    # 2. Partition - Re-seleciona faces a cada corte
    for d_id in datum_ids:
        # Seleciona todas as faces atuais
        faces_to_partition = tuple(p.faces[:])
        p.PartitionFaceByDatumPlane(datumPlane=p.datums[d_id],
                                    faces=faces_to_partition)
        p.regenerate()

    print("Partitions concluded for part: {}".format(part_name))


def CreateSetforLayers(modelName, part_name, layer_depths, top_depth, base_depth, inner_radius, thickness):
    p = mdb.models[modelName].parts[part_name]
    all_depths = sorted([top_depth, base_depth] + layer_depths)
    # all_depths = sorted([part_data["top_depth"], part_data["base_depth"]] + part_data["layer_depths"])
    layer_info = []

    # Criar sets para cada camada
    for i in range(len(all_depths) - 1):
        # No sketch as coordenadas sao negativas
        top = all_depths[i]
        bottom = all_depths[i + 1]
        mid_depth = -(top + bottom) / 2.0
        mid_radius = inner_radius + thickness / 2.0

        # Coordenadas X (raio)
        # x_min = inner_radius
        # x_max = inner_radius + thickness

        # Nome unico: SET_ROCK_LAYER_PROF1_PROF2
        set_name = 'SET_%s_Layer_%d_%d' % (part_name, int(top), int(bottom))

        # Captura a face que contém o ponto médio da camada
        faces_in_layer = p.faces.findAt(((mid_radius, mid_depth, 0.0), ))

        if faces_in_layer:
            p.Set(faces=faces_in_layer, name=set_name)
            print("Set criado com sucesso: %s" % (set_name))
        # else:
        #     mid_y = (top + bottom) / 2.0
        #     mid_x = (x_min + x_max) / 2.0
        #     try:
        #         f = p.faces.findAt(((mid_x, mid_y, 0.0), ))
        #         p.Set(faces=p.faces[f.index:f.index+1], name=set_name)
        #         print("Set criado via findAt: %s" % set_name)
        #     except:
        #         print("ERRO CRITICO: Nao foi possivel encontrar face para %s" % set_name)

        layer_info.append({
            "set_name": set_name,
            "top_depth": top,
            "base_depth": bottom
        })

    return layer_info


if __name__ == "__main__":
    example = {
        "pipe_inner_radius": 0.11,
        "annular_radius": 0.13,
        "rock_radius": 0.14,
        "base_depth": 4000,
        "top_depth": 3200,
        "pipe_wt": 0.02,
        "fluid_wt": 0.01,
        "rock_wt": 14.87
    }

    layers_depths = [3300, 3550, 3600]

    data = {
        "ROCK": {"inner_radius": example["rock_radius"],
                 "top_depth": example["top_depth"],
                 "base_depth": example["base_depth"],
                 "thickness": example["rock_wt"],
                 "layer_depths": layers_depths
                 },

        "FLUID": {"inner_radius": example["annular_radius"],
                  "top_depth": example["top_depth"],
                  "base_depth": example["base_depth"],
                  "thickness": example["fluid_wt"],
                  "layer_depths": layers_depths
                  },
        "PIPE": {"inner_radius": example["pipe_inner_radius"],
                 "top_depth": example["top_depth"],
                 "base_depth": example["base_depth"],
                 "thickness": example["pipe_wt"],
                 "layer_depths": layers_depths
                 },
    }

    name_model = 'MyFirstModel'
    if name_model not in mdb.models:
        mdb.Model(name=name_model, modelType=STANDARD_EXPLICIT)
    for part_name, part_data in data.items():
        CreateGeometry(name_model, part_name, part_data)
    # if part_name == 'ROCK':
        PartitionLayersByDepth(
            name_model, part_name=part_name, layer_depths=part_data["layer_depths"])
        layers_info = CreateSetforLayers(name_model, part_name=part_name, layer_depths=part_data["layer_depths"],
                                         top_depth=part_data["top_depth"], base_depth=part_data["base_depth"],
                                         inner_radius=part_data["inner_radius"], thickness=part_data["thickness"])
    # print('Geometry created in:', mdb.models['MyFirstModel'])
mdb.saveAs(pathName='FEM_AXYS_WELL_SHIELD.cae')
