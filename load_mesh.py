import numpy as np
from typing import Union

def translate(points, xyz: Union[list, tuple, np.ndarray]):
    """Translate the mesh.
    Parameters
    ----------
    xyz : list or tuple or np.ndarray
        Length 3 list, tuple or array.
    """
    points += np.asarray(xyz)

# def rotate_z(self, angle):
#     """Rotate mesh about the z-axis.
#
#     Parameters
#     ----------
#     angle : float
#         Angle in degrees to rotate about the z-axis.
#
#     """
#     axis_rotation(self.points, angle, inplace=True, axis='z')

def axis_rotation(points, angle, inplace=False, deg=True, axis='z'):
    """Rotate points angle (in deg) about an axis."""
    axis = axis.lower()

    # Copy original array to if not inplace
    if not inplace:
        points = points.copy()

    # Convert angle to radians
    if deg:
        angle *= np.pi / 180

    if axis == 'x':
        y = points[:, 1] * np.cos(angle) - points[:, 2] * np.sin(angle)
        z = points[:, 1] * np.sin(angle) + points[:, 2] * np.cos(angle)
        points[:, 1] = y
        points[:, 2] = z
    elif axis == 'y':
        x = points[:, 0] * np.cos(angle) + points[:, 2] * np.sin(angle)
        z = - points[:, 0] * np.sin(angle) + points[:, 2] * np.cos(angle)
        points[:, 0] = x
        points[:, 2] = z
    elif axis == 'z':
        x = points[:, 0] * np.cos(angle) - points[:, 1] * np.sin(angle)
        y = points[:, 0] * np.sin(angle) + points[:, 1] * np.cos(angle)
        points[:, 0] = x
        points[:, 1] = y
    else:
        raise Exception('invalid axis.  Must be either "x", "y", or "z"')

    if not inplace:
        return points

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
# with open("smpl_re.obj", 'w') as fp:
#     for v in verts:
#         fp.write('v %f %f %f\n' % (v[0], v[1], v[2]))
#
#     for f in faces + 1:
#         fp.write('f %d %d %d\n' % (f[0], f[1], f[2]))

axis_rotation(verts,358, inplace=True, deg=True, axis='z')
# translate(verts,(0.5,0.5,0.5))
with open("smpl_re.obj", 'w') as fp:
    for v in verts:
        fp.write('v %f %f %f\n' % (v[0], v[1], v[2]))

    for f in faces + 1:
        fp.write('f %d %d %d\n' % (f[0], f[1], f[2]))