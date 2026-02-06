from abaqus import *
from abaqusConstants import *

# import os
import sys 

path_project = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_'
# path_project = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_'

if path_project not in sys.path:
    sys.path.append(path_project)

# from GEOMETRY.geometries import Pipe
# from GEOMETRY.geometries import Fluid
# from GEOMETRY.geometries import Rock
from GEOMETRY.geometries import * 
from GEOMETRY.materials import *
from GEOMETRY.assembly import *
# from materials_novo import ElasticMaterial


mdb.models.changeKey(fromName='Model-1', toName='MyFirstModel')

if 'MyFirstModel' not in mdb.models:
    mdb.Model(name='MyFirstModel')

# variables that have to be changed ####################################################

inner_radius_pipe = 0.36829999999999996  # Updated by script
thickness_pipe = 0.00032258  # Updated by script
inner_radius_annular = inner_radius_pipe + thickness_pipe
# thickness_annular = 0.02
# inner_radius_wellbore = inner_radius_annular + thickness_annular
inner_radius_wellbore = 0.011612879999999999  # Updated by script
thickness_annular = inner_radius_wellbore - inner_radius_annular
thickness_wellbore = 12.0

base_depth = 4250.0  # Updated by script
top_depth = 3200.0  # Updated by script

########################################################################################

Pipe('MyFirstModel', 'PIPE', inner_radius_pipe, base_depth, top_depth, thickness_pipe)
Fluid('MyFirstModel', 'FLUID', inner_radius_annular, base_depth, top_depth, thickness_annular)
Rock('MyFirstModel', 'ROCK', inner_radius_wellbore, base_depth, top_depth, thickness_wellbore)


# if __name__ == "__main__":
#     example = {
#         "pipe_inner_radius": 0.11,
#         "annular_radius": 0.13,
#         "rock_radius": 0.14,
#         "base_depth": 3600,
#         "top_depth": 3200,
#         "pipe_wt": 0.02,
#         "fluid_wt": 0.01,
#         "rock_wt": 14.87
#     }

#     layers_depths = [3300, 3400, 3500]

#     data = {
#         "ROCK": {"inner_radius": example["rock_radius"],
#                  "top_depth": example["top_depth"],
#                  "base_depth": example["base_depth"],
#                  "thickness": example["rock_wt"],
#                  "layer_depths": layers_depths
#                  },

#         "FLUID": {"inner_radius": example["annular_radius"],
#                   "top_depth": example["top_depth"],
#                   "base_depth": example["base_depth"],
#                   "thickness": example["fluid_wt"],
#                   "layer_depths": layers_depths
#                   },
#         "PIPE": {"inner_radius": example["pipe_inner_radius"],
#                  "top_depth": example["top_depth"],
#                  "base_depth": example["base_depth"],
#                  "thickness": example["pipe_wt"],
#                  "layer_depths": layers_depths
#                  },
#     }
    
#     # if 'MyFirstModel' not in mdb.models:
#     #     mdb.Model(name='MyFirstModel', modelType=STANDARD_EXPLICIT)
#     for part_name, part_data in data.items():
#         CreateGeometry('MyFirstModel', part_name, part_data)
#         PartitionLayersByDepth("MyFirstModel", part_name=part_name, layer_depths=part_data["layer_depths"])

# if __name__ == "__main__":
#     examples = {
#         "ELASTIC_MAT": {
#             "behavior": "Elastic",
#             'density': 7800,
#             'elastic': (210000, 0.3),
#             'conductivity': 45,
#             'specific_heat': 500,
#             'expansion': 1.2e-5
#         },
#         "VONMISES_MAT": {
#             "behavior": "vonMises",
#             'density': 7800,
#             'elastic': (210000, 0.3),
#             'conductivity': 45,
#             'specific_heat': 500,
#             'expansion': 1.2e-5,
#             'stress_strain_curve': ((250, 0.0), (300, 0.02), (350, 0.05), (400, 0.1))
#         },
#         "MOHRCOULOMB_MAT": {
#             "behavior": "MohrCoulomb",
#             'density': 2000,
#             'elastic': (15400e6, 0.14),
#             'conductivity': 1.1,
#             'specific_heat': 2100,
#             'expansion': 0.0,
#             'friction_angle': 30.0,
#             'dilatancy_angle': 10.0,
#             'cohesion': 5e6,
#             'lab_data': ((10e6, 0.0), (20e6, 0.01), (30e6, 0.03), (40e6, 0.06))
#         },
#         "DOUBLE_POWER_CREEP_MAT": {
#             "behavior": "DoublePowerCreep",
#             "density": 2170.23,
#             "elastic": (20403e6, 0.36),
#             "conductivity": 5.685,
#             "specific_heat": 880.25,
#             "expansion": 0.0,
#             "creep_parameters": {
#                 "A1": 1.0,
#                 "A2": 2.0,
#                 "B1": 3.0,
#                 "B2": 4.0,
#                 "C1": 5.0,
#                 "C2": 6.0,
#                 "reference_stress": 100.0
#             }
#         },
#         "DOUBLE_MECHANISM_CREEP_MAT": {
#             "behavior": "DoubleMechanismCreep",
#             "density": 2170.23,
#             "elastic": (20403e6, 0.36),
#             "conductivity": 5.685,
#             "specific_heat": 880.25,
#             "expansion": 0.0,
#             "creep_parameters": {
#                 "reference_strain": 1.0,
#                 "reference_stress": 100.0,
#                 "reference_temperature": 293.0,
#                 "N1": 2.0,
#                 "N2": 4.0,
#                 "Q": 3.0,
#                 "R": 5.0,
#             },
#         }
#     }
#     material_examples = {
#         "PIPE": {
#             "partName": 'PIPE',
#             "sectionName": 'VONMISES_MAT_Section',
#             "isSolid": True
#         },
#         "FLUID": {
#             "partName": 'FLUID',
#             "sectionName": 'ELASTIC_MAT_Section',
#             "isSolid": True
#         },
#         "ROCK": {
#             "partName": 'ROCK',
#             "sectionName": 'DOUBLE_POWER_CREEP_MAT_Section',
#             "isSolid": True
#         }
#     }

#     # if 'MyFirstModel' not in mdb.models:
#     #     mdb.Model(name='MyFirstModel')

#     for mat_name, mat_data in examples.items():
#         CreateMaterial('MyFirstModel', mat_name, mat_data, sectionLength=1.)
#     for section_name in material_examples.values():
#         Assign_Section('MyFirstModel',
#                        partName=section_name["partName"],
#                        sectionName=section_name["sectionName"],
#                        isSolid=section_name["isSolid"])