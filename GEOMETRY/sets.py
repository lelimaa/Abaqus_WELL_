from abaqus import mdb
from abaqusConstants import *

    session.viewports['Viewport: 1'].view.setValues(nearPlane=1887.87, 
        farPlane=3148.73, width=4.63154, height=2.09147, cameraPosition=(
        1.46594, -6243.3, 2.13651), cameraTarget=(1.46594, -3723.2, 0.0258625))
    p1 = mdb.models['MyFirstModel'].parts['FLUID']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1888.05, 
        farPlane=3148.55, width=2.41492, height=1.09051, cameraPosition=(
        0.676116, -6243.3, 2.12438), cameraTarget=(0.676116, -3723.2, 
        0.0137331))
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
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
    p.Set(edges=edges, name='FASEI_OPEN_WELL')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    p.Set(faces=faces, name='ALLROCK')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1887.73, 
        farPlane=3148.87, width=5.44236, height=2.45761, cameraPosition=(
        1.39037, -6243.3, 2.104), cameraTarget=(1.39037, -3723.2, -0.00665549))
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#20 ]', ), )
    p.Set(edges=edges, name='L1-I_BASE')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#200 ]', ), )
    p.Set(edges=edges, name='L1-I_ID')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1886.63, 
        farPlane=3149.97, width=18.156, height=8.19872, cameraPosition=(
        5.78218, -6243.3, 3.30278), cameraTarget=(5.78218, -3723.2, 1.19213))
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1887.78, 
        farPlane=3148.82, width=4.95113, height=2.23579, cameraPosition=(
        2.04034, -6243.3, 2.31539), cameraTarget=(2.04034, -3723.2, 0.20474))
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Set(edges=edges, name='L2-I_BASE')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#40 ]', ), )
    p.Set(edges=edges, name='L2-I_ID')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1887.05, 
        farPlane=3149.55, width=16.752, height=7.56471, cameraPosition=(
        5.99645, -6243.3, 2.50852), cameraTarget=(5.99645, -3723.2, 0.397873))
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