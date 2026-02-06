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
thickness_pipe = 0.0127  # Updated by script
inner_radius_annular = inner_radius_pipe + thickness_pipe
# thickness_annular = 0.02
# inner_radius_wellbore = inner_radius_annular + thickness_annular
inner_radius_wellbore = 0.011612879999999999  # Updated by script
thickness_annular = inner_radius_wellbore - inner_radius_annular
thickness_wellbore = 12.0

base_depth = 4250.0  # Updated by script
base_depth = int(base_depth)
top_depth = 3200.0  # Updated by script
top_depth = int(top_depth)

########################################################################################

# Pipe('MyFirstModel', 'PIPE', inner_radius_pipe, base_depth, top_depth, thickness_pipe)
# Fluid('MyFirstModel', 'FLUID', inner_radius_annular, base_depth, top_depth, thickness_annular)
# Rock('MyFirstModel', 'ROCK', inner_radius_wellbore, base_depth, top_depth, thickness_wellbore)

########################################################################################

if __name__ == "__main__":
    example = {
        "pipe_inner_radius": inner_radius_pipe,
        "annular_radius": inner_radius_annular,
        "rock_radius": inner_radius_wellbore,
        "base_depth": base_depth,
        "top_depth": top_depth,
        "pipe_wt": thickness_pipe,
        "fluid_wt": thickness_annular,
        "rock_wt": thickness_wellbore
    }

    layers_depths = [3300, 3600, 4000]

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

for part_name, part_data in data.items():
        CreateGeometry('MyFirstModel', part_name, part_data)
        PartitionLayersByDepth("MyFirstModel", part_name=part_name, layer_depths=part_data["layer_depths"])

Assembly('MyFirstModel', ['FLUID', 'PIPE', 'ROCK'])