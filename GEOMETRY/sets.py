from abaqus import mdb
from abaqusConstants import *

def CreateSetsPipe(name_model):
    m = mdb.models[name_model]
    p = m.parts['PIPE']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    p.Set(faces=faces, name='FASEI_REV')
    faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    p.Set(faces=faces, name='FASEI_REV_ABOVE_TOC')
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
    p.Set(edges=edges, name='FASEI_REV_BASE')
    edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
    p.Set(edges=edges, name='FASEI_REV_ID')
    edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
    p.Set(edges=edges, name='FASEI_REV_OD')
    edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
    p.Set(edges=edges, name='FASEI_REV_TOP')
    edges = e.getSequenceFromMask(mask=('[#125 ]', ), )
    p.Set(edges=edges, name='FASEI_REV_TT')
    edges1 = e1.getSequenceFromMask(mask=('[#125 ]', ), )
    a = m.rootAssembly
    a.Set(edges=edges1, name='MESH_TT_PIPES')
    e1 = a.instances['PIPE_INST'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#242 ]', ), )
    a.Set(edges=edges1, name='FASEI_COMPLETED_WELL')   
    # a1 = m.rootAssembly
    # a1.regenerate()
    # a.regenerate()
    # p = m.parts['PIPE']
    # p = m.parts['PIPE']
    # f = p.faces
    # p = m.parts['PIPE']
    # e = p.edges
    # p = m.parts['PIPE']
    # e = p.edges
    # p = m.parts['PIPE']
    # e = p.edges
    # p = m.parts['PIPE']
    # e = p.edges
    # p = m.parts['PIPE']
    # e = p.edges
    # a = m.rootAssembly
    # e1 = a.instances['PIPE_INST'].edges
    

# def create_sets_fluid(name_model):
#     m = mdb.models[name_model]
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
#     p.Set(edges=edges, name='FASEI_OPEN_WELL')
#     p = m.parts['ROCK']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
#     p.Set(faces=faces, name='ALLROCK')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#20 ]', ), )
#     p.Set(edges=edges, name='L1-I_BASE')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#200 ]', ), )
#     p.Set(edges=edges, name='L1-I_ID')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#80 ]', ), )
#     p.Set(edges=edges, name='L1-I_OD')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
#     p.Set(edges=edges, name='L1-I_TOP')
#     p = m.parts['ROCK']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#4 ]', ), )
#     p.Set(faces=faces, name='L1-I')
#     p = m.parts['ROCK']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
#     p.Set(faces=faces, name='L2-I')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
#     p.Set(edges=edges, name='L2-I_BASE')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#40 ]', ), )
#     p.Set(edges=edges, name='L2-I_ID')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#10 ]', ), )
#     p.Set(edges=edges, name='L2-I_OD')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#20 ]', ), )
#     p.Set(edges=edges, name='L2-I_TOP')
#     p = m.parts['ROCK']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
#     p.Set(faces=faces, name='L3-I')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
#     p.Set(edges=edges, name='L3-I_BASE')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#2 ]', ), )
#     p.Set(edges=edges, name='L3-I_ID')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#8 ]', ), )
#     p.Set(edges=edges, name='L3-I_OD')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
#     p.Set(edges=edges, name='L3-I_TOP')
#     p = m.parts['FLUID']
#     p = m.parts['FLUID']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
#     p.Set(faces=faces, name='FASEI_FLUIDO')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
#     p.Set(edges=edges, name='FASEI_FLUIDO_BASE')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
#     p.Set(edges=edges, name='FASEI_FLUIDO_ID')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
#     p.Set(edges=edges, name='FASEI_FLUIDO_OD')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
#     p.Set(edges=edges, name='FASEI_FLUIDO_TOP')
#     p = m.parts['PIPE']
#     a1 = m.rootAssembly
#     a1.regenerate()
#     a = m.rootAssembly
#     p1 = m.parts['ROCK']
#     p = m.parts['PIPE']
#     p = m.parts['ROCK']
#     p = m.parts['PIPE']
#     p = m.parts['FLUID']
#     p = m.parts['PIPE']
#     p1 = m.parts['ROCK']
#     p = m.parts['PIPE']
#     p1 = m.parts['ROCK']
#     p = m.parts['PIPE']
#     a = m.rootAssembly
#     a = m.rootAssembly
#     a = m.rootAssembly
#     f1 = a.instances['FLUID_INST'].faces
#     faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
#     f2 = a.instances['PIPE_INST'].faces
#     faces2 = f2.getSequenceFromMask(mask=('[#7 ]', ), )
#     a.Set(faces=faces1+faces2, name='FASEI')
#     p1 = m.parts['FLUID']
#     p = m.parts['FLUID']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
#     p.Set(faces=faces, name='FASEI_ANNULAR')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
#     p.Set(edges=edges, name='FASEI_ANNULAR_BASE')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
#     p.Set(edges=edges, name='FASEI_ANNULAR_ID')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
#     p.Set(edges=edges, name='FASEI_ANNULAR_OD')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
#     p.Set(edges=edges, name='FASEI_ANNULAR_TOP')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#125 ]', ), )
#     p.Set(edges=edges, name='FASEI_ANNULAR_TT')
#     a = m.rootAssembly
#     a.regenerate()
#     a = m.rootAssembly
#     e1 = a.instances['PIPE_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#242 ]', ), )
#     a.Set(edges=edges1, name='FASEI_COMPLETED_WELL')
#     p1 = m.parts['ROCK']
#     a = m.rootAssembly
#     a = m.rootAssembly
#     f1 = a.instances['FLUID_INST'].faces
#     faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
#     f2 = a.instances['PIPE_INST'].faces
#     faces2 = f2.getSequenceFromMask(mask=('[#7 ]', ), )
#     f3 = a.instances['ROCK_INST'].faces
#     faces3 = f3.getSequenceFromMask(mask=('[#7 ]', ), )
#     r3 = a.instances['ROCK_INST'].referencePoints
#     refPoints3=(r3[2], )
#     a.Set(faces=faces1+faces2+faces3, referencePoints=refPoints3, name='ALL')

#     p = m.parts['PIPE']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
#     p.Set(faces=faces, name='FASEI_REV')
#     p = m.parts['PIPE']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
#     p.Set(faces=faces, name='FASEI_REV_ABOVE_TOC')
#     p = m.parts['PIPE']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
#     p.Set(edges=edges, name='FASEI_REV_BASE')
#     p = m.parts['PIPE']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
#     p.Set(edges=edges, name='FASEI_REV_ID')
#     p = m.parts['PIPE']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
#     p.Set(edges=edges, name='FASEI_REV_OD')
#     p = m.parts['PIPE']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
#     p.Set(edges=edges, name='FASEI_REV_TOP')
#     p = m.parts['PIPE']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#125 ]', ), )
#     p.Set(edges=edges, name='FASEI_REV_TT')
#     p = m.parts['ROCK']
#     p = m.parts['ROCK']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
#     p.Set(faces=faces, name='FASEI_SLAVE')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
#     p.Set(edges=edges, name='FASEI_WELL')
#     a = m.rootAssembly
#     a.regenerate()
#     a = m.rootAssembly
#     e1 = a.instances['FLUID_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#125 ]', ), )
#     a.Set(edges=edges1, name='MESH_TT_ANNULARS')
#     a = m.rootAssembly
#     e1 = a.instances['PIPE_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#125 ]', ), )
#     a.Set(edges=edges1, name='MESH_TT_PIPES')
#     a = m.rootAssembly
#     e1 = a.instances['ROCK_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#125 ]', ), )
#     a.Set(edges=edges1, name='MESH_TT_ROCK')
#     a = m.rootAssembly
#     e1 = a.instances['PIPE_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#2da ]', ), )
#     e2 = a.instances['ROCK_INST'].edges
#     edges2 = e2.getSequenceFromMask(mask=('[#2da ]', ), )
#     a.Set(edges=edges1+edges2, name='MESH_VERTICAL')
#     a = m.rootAssembly
#     r1 = a.instances['ROCK_INST'].referencePoints
#     refPoints1=(r1[2], )
#     a.Set(referencePoints=refPoints1, name='REFPT')
#     a = m.rootAssembly
#     e1 = a.instances['ROCK_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#98 ]', ), )
#     a.Set(edges=edges1, name='ROCK_BC')
#     a = m.rootAssembly
#     f1 = a.instances['ROCK_INST'].faces
#     faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
#     a.Set(faces=faces1, name='ROCK_OUTPUT')
#     a = m.rootAssembly
#     e1 = a.instances['PIPE_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
#     e2 = a.instances['FLUID_INST'].edges
#     edges2 = e2.getSequenceFromMask(mask=('[#4 ]', ), )
#     e3 = a.instances['ROCK_INST'].edges
#     edges3 = e3.getSequenceFromMask(mask=('[#4 ]', ), )
#     a.Set(edges=edges1+edges2+edges3, name='YSYM_BASE')
#     a = m.rootAssembly
#     e1 = a.instances['ROCK_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#100 ]', ), )
#     e2 = a.instances['FLUID_INST'].edges
#     edges2 = e2.getSequenceFromMask(mask=('[#100 ]', ), )
#     e3 = a.instances['PIPE_INST'].edges
#     edges3 = e3.getSequenceFromMask(mask=('[#100 ]', ), )
#     a.Set(edges=edges1+edges2+edges3, name='YSYM_TOP')

# def create_sets_rock(name_model):
#     m = mdb.models[name_model]
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
#     p.Set(edges=edges, name='FASEI_OPEN_WELL')
#     p = m.parts['ROCK']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
#     p.Set(faces=faces, name='ALLROCK')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#20 ]', ), )
#     p.Set(edges=edges, name='L1-I_BASE')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#200 ]', ), )
#     p.Set(edges=edges, name='L1-I_ID')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#80 ]', ), )
#     p.Set(edges=edges, name='L1-I_OD')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
#     p.Set(edges=edges, name='L1-I_TOP')
#     p = m.parts['ROCK']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#4 ]', ), )
#     p.Set(faces=faces, name='L1-I')
#     p = m.parts['ROCK']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
#     p.Set(faces=faces, name='L2-I')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
#     p.Set(edges=edges, name='L2-I_BASE')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#40 ]', ), )
#     p.Set(edges=edges, name='L2-I_ID')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#10 ]', ), )
#     p.Set(edges=edges, name='L2-I_OD')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#20 ]', ), )
#     p.Set(edges=edges, name='L2-I_TOP')
#     p = m.parts['ROCK']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
#     p.Set(faces=faces, name='L3-I')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
#     p.Set(edges=edges, name='L3-I_BASE')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#2 ]', ), )
#     p.Set(edges=edges, name='L3-I_ID')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#8 ]', ), )
#     p.Set(edges=edges, name='L3-I_OD')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
#     p.Set(edges=edges, name='L3-I_TOP')
#     p = m.parts['FLUID']
#     p = m.parts['FLUID']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
#     p.Set(faces=faces, name='FASEI_FLUIDO')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
#     p.Set(edges=edges, name='FASEI_FLUIDO_BASE')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
#     p.Set(edges=edges, name='FASEI_FLUIDO_ID')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
#     p.Set(edges=edges, name='FASEI_FLUIDO_OD')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
#     p.Set(edges=edges, name='FASEI_FLUIDO_TOP')
#     p = m.parts['PIPE']
#     a1 = m.rootAssembly
#     a1.regenerate()
#     a = m.rootAssembly
#     p1 = m.parts['ROCK']
#     p = m.parts['PIPE']
#     p = m.parts['ROCK']
#     p = m.parts['PIPE']
#     p = m.parts['FLUID']
#     p = m.parts['PIPE']
#     p1 = m.parts['ROCK']
#     p = m.parts['PIPE']
#     p1 = m.parts['ROCK']
#     p = m.parts['PIPE']
#     a = m.rootAssembly
#     a = m.rootAssembly
#     a = m.rootAssembly
#     f1 = a.instances['FLUID_INST'].faces
#     faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
#     f2 = a.instances['PIPE_INST'].faces
#     faces2 = f2.getSequenceFromMask(mask=('[#7 ]', ), )
#     a.Set(faces=faces1+faces2, name='FASEI')
#     p1 = m.parts['FLUID']
#     p = m.parts['FLUID']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
#     p.Set(faces=faces, name='FASEI_ANNULAR')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
#     p.Set(edges=edges, name='FASEI_ANNULAR_BASE')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
#     p.Set(edges=edges, name='FASEI_ANNULAR_ID')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
#     p.Set(edges=edges, name='FASEI_ANNULAR_OD')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
#     p.Set(edges=edges, name='FASEI_ANNULAR_TOP')
#     p = m.parts['FLUID']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#125 ]', ), )
#     p.Set(edges=edges, name='FASEI_ANNULAR_TT')
#     a = m.rootAssembly
#     a.regenerate()
#     a = m.rootAssembly
#     e1 = a.instances['PIPE_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#242 ]', ), )
#     a.Set(edges=edges1, name='FASEI_COMPLETED_WELL')
#     p1 = m.parts['ROCK']
#     a = m.rootAssembly
#     a = m.rootAssembly
#     f1 = a.instances['FLUID_INST'].faces
#     faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
#     f2 = a.instances['PIPE_INST'].faces
#     faces2 = f2.getSequenceFromMask(mask=('[#7 ]', ), )
#     f3 = a.instances['ROCK_INST'].faces
#     faces3 = f3.getSequenceFromMask(mask=('[#7 ]', ), )
#     r3 = a.instances['ROCK_INST'].referencePoints
#     refPoints3=(r3[2], )
#     a.Set(faces=faces1+faces2+faces3, referencePoints=refPoints3, name='ALL')

#     p = m.parts['PIPE']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
#     p.Set(faces=faces, name='FASEI_REV')
#     p = m.parts['PIPE']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
#     p.Set(faces=faces, name='FASEI_REV_ABOVE_TOC')
#     p = m.parts['PIPE']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
#     p.Set(edges=edges, name='FASEI_REV_BASE')
#     p = m.parts['PIPE']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
#     p.Set(edges=edges, name='FASEI_REV_ID')
#     p = m.parts['PIPE']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
#     p.Set(edges=edges, name='FASEI_REV_OD')
#     p = m.parts['PIPE']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
#     p.Set(edges=edges, name='FASEI_REV_TOP')
#     p = m.parts['PIPE']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#125 ]', ), )
#     p.Set(edges=edges, name='FASEI_REV_TT')
#     p = m.parts['ROCK']
#     p = m.parts['ROCK']
#     f = p.faces
#     faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
#     p.Set(faces=faces, name='FASEI_SLAVE')
#     p = m.parts['ROCK']
#     e = p.edges
#     edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
#     p.Set(edges=edges, name='FASEI_WELL')
#     a = m.rootAssembly
#     a.regenerate()
#     a = m.rootAssembly
#     e1 = a.instances['FLUID_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#125 ]', ), )
#     a.Set(edges=edges1, name='MESH_TT_ANNULARS')
#     a = m.rootAssembly
#     e1 = a.instances['PIPE_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#125 ]', ), )
#     a.Set(edges=edges1, name='MESH_TT_PIPES')
#     a = m.rootAssembly
#     e1 = a.instances['ROCK_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#125 ]', ), )
#     a.Set(edges=edges1, name='MESH_TT_ROCK')
#     a = m.rootAssembly
#     e1 = a.instances['PIPE_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#2da ]', ), )
#     e2 = a.instances['ROCK_INST'].edges
#     edges2 = e2.getSequenceFromMask(mask=('[#2da ]', ), )
#     a.Set(edges=edges1+edges2, name='MESH_VERTICAL')
#     a = m.rootAssembly
#     r1 = a.instances['ROCK_INST'].referencePoints
#     refPoints1=(r1[2], )
#     a.Set(referencePoints=refPoints1, name='REFPT')
#     a = m.rootAssembly
#     e1 = a.instances['ROCK_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#98 ]', ), )
#     a.Set(edges=edges1, name='ROCK_BC')
#     a = m.rootAssembly
#     f1 = a.instances['ROCK_INST'].faces
#     faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
#     a.Set(faces=faces1, name='ROCK_OUTPUT')
#     a = m.rootAssembly
#     e1 = a.instances['PIPE_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
#     e2 = a.instances['FLUID_INST'].edges
#     edges2 = e2.getSequenceFromMask(mask=('[#4 ]', ), )
#     e3 = a.instances['ROCK_INST'].edges
#     edges3 = e3.getSequenceFromMask(mask=('[#4 ]', ), )
#     a.Set(edges=edges1+edges2+edges3, name='YSYM_BASE')
#     a = m.rootAssembly
#     e1 = a.instances['ROCK_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#100 ]', ), )
#     e2 = a.instances['FLUID_INST'].edges
#     edges2 = e2.getSequenceFromMask(mask=('[#100 ]', ), )
#     e3 = a.instances['PIPE_INST'].edges
#     edges3 = e3.getSequenceFromMask(mask=('[#100 ]', ), )
#     a.Set(edges=edges1+edges2+edges3, name='YSYM_TOP')

# def create_sets_assembly(name_model):  
#     m = mdb.models[name_model]  
#     a = m.rootAssembly
#     f1 = a.instances['FLUID_INST'].faces
#     faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
#     f2 = a.instances['PIPE_INST'].faces
#     faces2 = f2.getSequenceFromMask(mask=('[#7 ]', ), )
#     a.Set(faces=faces1+faces2, name='FASEI')
#     a = m.rootAssembly
#     f1 = a.instances['FLUID_INST'].faces
#     faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
#     f2 = a.instances['PIPE_INST'].faces
#     faces2 = f2.getSequenceFromMask(mask=('[#7 ]', ), )
#     f3 = a.instances['ROCK_INST'].faces
#     faces3 = f3.getSequenceFromMask(mask=('[#7 ]', ), )
#     r3 = a.instances['ROCK_INST'].referencePoints
#     refPoints3=(r3[2], )
#     a.Set(faces=faces1+faces2+faces3, referencePoints=refPoints3, name='ALL')

#     a = m.rootAssembly
#     e1 = a.instances['PIPE_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#2da ]', ), )
#     e2 = a.instances['ROCK_INST'].edges
#     edges2 = e2.getSequenceFromMask(mask=('[#2da ]', ), )
#     a.Set(edges=edges1+edges2, name='MESH_VERTICAL')

#     a = m.rootAssembly
#     e1 = a.instances['PIPE_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
#     e2 = a.instances['FLUID_INST'].edges
#     edges2 = e2.getSequenceFromMask(mask=('[#4 ]', ), )
#     e3 = a.instances['ROCK_INST'].edges
#     edges3 = e3.getSequenceFromMask(mask=('[#4 ]', ), )
#     a.Set(edges=edges1+edges2+edges3, name='YSYM_BASE')

#     a = m.rootAssembly
#     e1 = a.instances['ROCK_INST'].edges
#     edges1 = e1.getSequenceFromMask(mask=('[#100 ]', ), )
#     e2 = a.instances['FLUID_INST'].edges
#     edges2 = e2.getSequenceFromMask(mask=('[#100 ]', ), )
#     e3 = a.instances['PIPE_INST'].edges
#     edges3 = e3.getSequenceFromMask(mask=('[#100 ]', ), )
#     a.Set(edges=edges1+edges2+edges3, name='YSYM_TOP')