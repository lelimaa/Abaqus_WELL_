from abaqus import *
from abaqusConstants import *

# import os
import sys 

path_project = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_'

if path_project not in sys.path:
    sys.path.append(path_project)

# from assembly import Assembly
from GEOMETRY.geometries import Pipe
# from materials_novo import ElasticMaterial

# Pipe('MyFirstModel', 'PIPE', inner_radius=0.05, base_depth=3600, top_depth=3200, thickness=0.02)