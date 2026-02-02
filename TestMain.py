from abaqus import *
from abaqusConstants import *

# import os
import sys 

path_project = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_'
# path_project = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_'

if path_project not in sys.path:
    sys.path.append(path_project)

from GEOMETRY.geometries import Pipe
from GEOMETRY.geometries import Fluid
from GEOMETRY.geometries import Rock
from GEOMETRY.assembly import Assembly
# from materials_novo import ElasticMaterial


mdb.models.changeKey(fromName='Model-1', toName='MyFirstModel')

# if 'MyFirstModel' not in mdb.models:
#     mdb.Model(name='MyFirstModel')

inner_radius_pipe = 0.05
thickness_pipe = 0.01
inner_radius_annular = inner_radius_pipe + thickness_pipe
thickness_annular = 0.02
inner_radius_wellbore = inner_radius_annular + thickness_annular
thickness_wellbore = 0.5

base_depth = 3600
top_depth = 3200


Pipe('MyFirstModel', 'PIPE', inner_radius_pipe, base_depth, top_depth, thickness_pipe)
Fluid('MyFirstModel', 'FLUID', inner_radius_annular, base_depth, top_depth, thickness_annular)
Rock('MyFirstModel', 'ROCK', inner_radius_wellbore, base_depth, top_depth, thickness_wellbore)

