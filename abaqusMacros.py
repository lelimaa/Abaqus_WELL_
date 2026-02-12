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


