from abaqus import mdb
from abaqusConstants import *

def CreateSetsPipe(name_model):
    m = mdb.models[name_model]
    p = m.parts['PIPE']
    f = p.faces
    e = p.edges

    # faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    # p.Set(faces=faces, name='FASEI_REV')
    # faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    # p.Set(faces=faces, name='FASEI_REV_ABOVE_TOC')
    all_faces = f[0:len(f)]
    p.Set(faces=all_faces, name='FASEI_REV')
    p.Set(faces=all_faces, name='FASEI_REV_ABOVE_TOC')


    # edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
    # p.Set(edges=edges, name='FASEI_REV_BASE')    
    tol = 0.001
    e = p.edges
    all_coords = [v.pointOn[0][1] for v in p.vertices]
    min_y_global = min(all_coords)
    base_edges = e.getByBoundingBox(
        xMin = -1e20, yMin=min_y_global - tol, zMin=-tol,
        xMax = 1e20, yMax=min_y_global + tol, zMax=tol
    )
    p.Set(edges=base_edges, name='FASEI_REV_BASE')

    # edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
    # p.Set(edges=edges, name='FASEI_REV_ID')
    all_x_coords = [v.pointOn[0][0] for v in p.vertices]
    min_x_global = min(all_x_coords)
    left_edges = e.getByBoundingBox(
        xMin=min_x_global - tol, yMin=-1e20, zMin=-tol,
        xMax=min_x_global + tol, yMax=1e20, zMax=tol
    )
    p.Set(edges=left_edges, name='FASEI_REV_ID')


    # edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
    # p.Set(edges=edges, name='FASEI_REV_OD')
    max_x_global = max([v.pointOn[0][0] for v in p.vertices])
    right_edges = e.getByBoundingBox(
        xMin=max_x_global - tol, yMin=-1e20, zMin=-tol,
        xMax=max_x_global + tol, yMax=1e20, zMax=tol
    )
    p.Set(edges=right_edges, name='FASEI_REV_OD')


    # edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
    # p.Set(edges=edges, name='FASEI_REV_TOP')
    all_y = [v.pointOn[0][1] for v in p.vertices]
    max_y_global = max(all_y)

    top_edges = e.getByBoundingBox(
        xMin=-1e20, yMin=max_y_global - tol, zMin=-tol,
        xMax=1e20, yMax=max_y_global + tol, zMax=tol
    )
    p.Set(edges=top_edges, name='FASEI_REV_TOP')

    # edges = e.getSequenceFromMask(mask=('[#125 ]', ), )
    # p.Set(edges=edges, name='FASEI_REV_TT')
    horizontal_edges = []
    tol = 0.0001

    for edge in p.edges:
        v1_idx = edge.getVertices()[0]
        v2_idx = edge.getVertices()[1]
        y1 = p.vertices[v1_idx].pointOn[0][1]
        y2 = p.vertices[v2_idx].pointOn[0][1]

        if abs(y1 - y2) < tol:
            horizontal_edges.append(p.edges[edge.index:edge.index + 1])

    if horizontal_edges:
        all_horizontals = horizontal_edges[0]
        for i in range(1, len(horizontal_edges)):
            all_horizontals += horizontal_edges[i]
        p.Set(edges=all_horizontals, name='FASEI_REV_TT')

    

def CreateSetsFluid(name_model):
    m = mdb.models[name_model]
    p = m.parts['FLUID']
    f = p.faces
    e = p.edges

    # faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    # p.Set(faces=faces, name='FASEI_FLUIDO')
    all_faces = f[0:len(f)]
    p.Set(faces=all_faces, name='FASEI_FLUIDO')

    # edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
    # p.Set(edges=edges, name='FASEI_FLUIDO_BASE')
    tol = 0.001
    e = p.edges
    all_coords = [v.pointOn[0][1] for v in p.vertices]
    min_y_global = min(all_coords)
    base_edges = e.getByBoundingBox(
        xMin = -1e20, yMin=min_y_global - tol, zMin=-tol,
        xMax = 1e20, yMax=min_y_global + tol, zMax=tol
    )
    p.Set(edges=base_edges, name='FASEI_FLUIDO_BASE')


    # edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
    # p.Set(edges=edges, name='FASEI_FLUIDO_ID')
    all_x_coords = [v.pointOn[0][0] for v in p.vertices]
    min_x_global = min(all_x_coords)
    left_edges = e.getByBoundingBox(
        xMin=min_x_global - tol, yMin=-1e20, zMin=-tol,
        xMax=min_x_global + tol, yMax=1e20, zMax=tol
    )
    p.Set(edges=left_edges, name='FASEI_FLUIDO_ID')



    # edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
    # p.Set(edges=edges, name='FASEI_FLUIDO_OD')
    max_x_global = max([v.pointOn[0][0] for v in p.vertices])
    right_edges = e.getByBoundingBox(
        xMin=max_x_global - tol, yMin=-1e20, zMin=-tol,
        xMax=max_x_global + tol, yMax=1e20, zMax=tol
    )
    p.Set(edges=right_edges, name='FASEI_FLUIDO_OD')

    # edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
    # p.Set(edges=edges, name='FASEI_FLUIDO_TOP')
    all_y = [v.pointOn[0][1] for v in p.vertices]
    max_y_global = max(all_y)

    top_edges = e.getByBoundingBox(
        xMin=-1e20, yMin=max_y_global - tol, zMin=-tol,
        xMax=1e20, yMax=max_y_global + tol, zMax=tol
    )
    p.Set(edges=top_edges, name='FASEI_FLUIDO_TOP')


    # a1 = m.rootAssembly
    # a1.regenerate()
    # a = m.rootAssembly
    # f1 = a.instances['FLUID_INST'].faces
    # faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
    # p1 = m.parts['FLUID']

    # f = p.faces
    # faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    # p.Set(faces=faces, name='FASEI_ANNULAR')
    all_faces = f[0:len(f)]
    p.Set(faces=all_faces, name='FASEI_ANNULAR')

    # edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
    # p.Set(edges=edges, name='FASEI_ANNULAR_BASE')
    tol = 0.001
    e = p.edges
    all_coords = [v.pointOn[0][1] for v in p.vertices]
    min_y_global = min(all_coords)
    base_edges = e.getByBoundingBox(
        xMin = -1e20, yMin=min_y_global - tol, zMin=-tol,
        xMax = 1e20, yMax=min_y_global + tol, zMax=tol
    )
    p.Set(edges=base_edges, name='FASEI_ANNULAR_BASE')

    # edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
    # p.Set(edges=edges, name='FASEI_ANNULAR_ID')
    all_x_coords = [v.pointOn[0][0] for v in p.vertices]
    min_x_global = min(all_x_coords)
    left_edges = e.getByBoundingBox(
        xMin=min_x_global - tol, yMin=-1e20, zMin=-tol,
        xMax=min_x_global + tol, yMax=1e20, zMax=tol
    )
    p.Set(edges=left_edges, name='FASEI_ANNULAR_ID')

    # edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
    # p.Set(edges=edges, name='FASEI_ANNULAR_OD')
    max_x_global = max([v.pointOn[0][0] for v in p.vertices])
    right_edges = e.getByBoundingBox(
        xMin=max_x_global - tol, yMin=-1e20, zMin=-tol,
        xMax=max_x_global + tol, yMax=1e20, zMax=tol
    )
    p.Set(edges=right_edges, name='FASEI_ANNULAR_OD')

    # edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
    # p.Set(edges=edges, name='FASEI_ANNULAR_TOP')
    all_y = [v.pointOn[0][1] for v in p.vertices]
    max_y_global = max(all_y)

    top_edges = e.getByBoundingBox(
        xMin=-1e20, yMin=max_y_global - tol, zMin=-tol,
        xMax=1e20, yMax=max_y_global + tol, zMax=tol
    )
    p.Set(edges=top_edges, name='FASEI_ANNULAR_TOP')


    # edges = e.getSequenceFromMask(mask=('[#125 ]', ), )
    # p.Set(edges=edges, name='FASEI_ANNULAR_TT')
    horizontal_edges = []
    tol = 0.0001

    for edge in p.edges:
        v1_idx = edge.getVertices()[0]
        v2_idx = edge.getVertices()[1]
        y1 = p.vertices[v1_idx].pointOn[0][1]
        y2 = p.vertices[v2_idx].pointOn[0][1]

        if abs(y1 - y2) < tol:
            horizontal_edges.append(p.edges[edge.index:edge.index + 1])

    if horizontal_edges:
        all_horizontals = horizontal_edges[0]
        for i in range(1, len(horizontal_edges)):
            all_horizontals += horizontal_edges[i]
        p.Set(edges=all_horizontals, name='FASEI_ANNULAR_TT')




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

    # a = m.rootAssembly
    # e1 = a.instances['ROCK_INST'].edges
    # edges1 = e1.getSequenceFromMask(mask=('[#100 ]', ), )
    # e2 = a.instances['FLUID_INST'].edges
    # edges2 = e2.getSequenceFromMask(mask=('[#100 ]', ), )
    # e3 = a.instances['PIPE_INST'].edges
    # edges3 = e3.getSequenceFromMask(mask=('[#100 ]', ), )
    # a.Set(edges=edges1+edges2+edges3, name='YSYM_TOP')

    # a = m.rootAssembly
    # e1 = a.instances['PIPE_INST'].edges
    # edges1 = e1.getSequenceFromMask(mask=('[#125 ]', ), )
    # a.Set(edges=edges1, name='MESH_TT_PIPES')
    # edges1 = e1.getSequenceFromMask(mask=('[#242 ]', ), )
    # a.Set(edges=edges1, name='FASEI_COMPLETED_WELL')  