# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def MacroSections():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    p = mdb.models['MyFirstModel'].parts['FLUID']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#f ]', ), )
    region = regionToolset.Region(faces=faces)
    p = mdb.models['MyFirstModel'].parts['FLUID']
    p.SectionAssignment(region=region, sectionName='FLUID_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p1 = mdb.models['MyFirstModel'].parts['PIPE']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['MyFirstModel'].parts['PIPE']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#f ]', ), )
    region = regionToolset.Region(faces=faces)
    p = mdb.models['MyFirstModel'].parts['PIPE']
    p.SectionAssignment(region=region, sectionName='STEEL_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p1 = mdb.models['MyFirstModel'].parts['ROCK']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1889.48, 
        farPlane=3151.08, width=6.55289, height=2.94006, cameraPosition=(
        0.550932, -6245.28, 1.9922), cameraTarget=(0.550932, -3725, 0.410418))
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#8 ]', ), )
    region = regionToolset.Region(faces=faces)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    p.SectionAssignment(region=region, sectionName='SHALE_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#4 ]', ), )
    region = regionToolset.Region(faces=faces)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    p.SectionAssignment(region=region, sectionName='SANDSTONE_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    region = regionToolset.Region(faces=faces)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    p.SectionAssignment(region=region, sectionName='SHALE_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(faces=faces)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    p.SectionAssignment(region=region, sectionName='HALITE_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def MacroAssembly():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    a1 = mdb.models['MyFirstModel'].rootAssembly
    p = mdb.models['MyFirstModel'].parts['FLUID']
    a1.Instance(name='FLUID-1', part=p, dependent=ON)
    a1 = mdb.models['MyFirstModel'].rootAssembly
    p = mdb.models['MyFirstModel'].parts['PIPE']
    a1.Instance(name='PIPE-1', part=p, dependent=ON)
    a1 = mdb.models['MyFirstModel'].rootAssembly
    p = mdb.models['MyFirstModel'].parts['ROCK']
    a1.Instance(name='ROCK-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1879.79, 
        farPlane=6245.21, width=2.38268, height=1.07595, cameraPosition=(
        0.620956, -6245, 1.32304), cameraTarget=(0.620956, -3724.8, 
        0.00520486))
    a1 = mdb.models['MyFirstModel'].rootAssembly
    a1.translate(instanceList=('ROCK-1', ), vector=(0.0, -10.0, 0.0))
    a1 = mdb.models['MyFirstModel'].rootAssembly
    a1.translate(instanceList=('ROCK-1', ), vector=(0.0, 10.0, 0.0))
    a = mdb.models['MyFirstModel'].rootAssembly
    a.deleteFeatures(('FLUID-1', 'PIPE-1', 'ROCK-1', ))
    a1 = mdb.models['MyFirstModel'].rootAssembly
    p = mdb.models['MyFirstModel'].parts['FLUID']
    a1.Instance(name='FLUID-1', part=p, dependent=ON)
    a1 = mdb.models['MyFirstModel'].rootAssembly
    p = mdb.models['MyFirstModel'].parts['PIPE']
    a1.Instance(name='PIPE-1', part=p, dependent=ON)
    a1 = mdb.models['MyFirstModel'].rootAssembly
    p = mdb.models['MyFirstModel'].parts['ROCK']
    a1.Instance(name='ROCK-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])


def MacroSets():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
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
