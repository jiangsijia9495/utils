import numpy as np

verts =np.zeros((1,3))
faces =np.zeros((1,3))
with open("smpl_np_org.obj","r") as fp:
    for line in fp:
        if line[0]=="v":
            l=line[2:].split()
            l=np.array(l).astype("float").reshape(1,3)
            verts = np.concatenate((verts,l),axis=0)
        if line[0]=="f":
            l=line[2:].split()
            l=(np.array(l).astype("int")-1).reshape(1,3)
            faces = np.concatenate((faces,l),axis=0)
verts = verts[1:]
faces = faces[1:]
with open("smpl_re.obj", 'w') as fp:
    for v in verts:
        fp.write('v %f %f %f\n' % (v[0], v[1], v[2]))

    for f in faces + 1:
        fp.write('f %d %d %d\n' % (f[0], f[1], f[2]))
