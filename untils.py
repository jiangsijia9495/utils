import trimesh
pointcloud = trimesh.points.PointCloud(render_out_fix['pts'].view(-1,3))
pointcloud.export('demo.ply')
from pytorch3d.structures import Pointclouds
pointclouds = Pointclouds(points=[torch.cat([render_out_fix['pts'].view(-1,3),render_out['your_pts']],dim=0)])
from pytorch3d.io import IO
IO().save_pointcloud(pointclouds, "output_pointcloud.ply")