from abaqus import mdb
from abaqusConstants import *

p = mdb.models['MyFirstModel'].parts['FLUID']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
p.Set(faces=faces, name='FASEI_FLUIDO')
p = mdb.models['MyFirstModel'].parts['FLUID']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_BASE')
p = mdb.models['MyFirstModel'].parts['FLUID']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_ID')
p = mdb.models['MyFirstModel'].parts['FLUID']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_OD')
p = mdb.models['MyFirstModel'].parts['FLUID']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_TOP')
p = mdb.models['MyFirstModel'].parts['ROCK']
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
p.Set(edges=edges, name='FASEI_OPEN_WELL')
p = mdb.models['MyFirstModel'].parts['ROCK']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
p.Set(faces=faces, name='ALLROCK')
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#20 ]', ), )
p.Set(edges=edges, name='L1-I_BASE')
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#200 ]', ), )
p.Set(edges=edges, name='L1-I_ID')
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#80 ]', ), )
p.Set(edges=edges, name='L1-I_OD')
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
p.Set(edges=edges, name='L1-I_TOP')
p = mdb.models['MyFirstModel'].parts['ROCK']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#4 ]', ), )
p.Set(faces=faces, name='L1-I')
p = mdb.models['MyFirstModel'].parts['ROCK']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
p.Set(faces=faces, name='L2-I')
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
p.Set(edges=edges, name='L2-I_BASE')
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#40 ]', ), )
p.Set(edges=edges, name='L2-I_ID')
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#10 ]', ), )
p.Set(edges=edges, name='L2-I_OD')
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#20 ]', ), )
p.Set(edges=edges, name='L2-I_TOP')
p = mdb.models['MyFirstModel'].parts['ROCK']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.Set(faces=faces, name='L3-I')
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
p.Set(edges=edges, name='L3-I_BASE')
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#2 ]', ), )
p.Set(edges=edges, name='L3-I_ID')
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#8 ]', ), )
p.Set(edges=edges, name='L3-I_OD')
p = mdb.models['MyFirstModel'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
p.Set(edges=edges, name='L3-I_TOP')