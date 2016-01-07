mepyDir = "E:\\My\\GitHub\\mepy"
import sys
sys.path.append(mepyDir)
import mepy
mepy.CleanCacheModules(mepyDir)

from Mesh import Mesh

mesh = Mesh()
mesh.Name = "polySurface1047"
vertexs = mesh.GetVertexsPos()
for v in vertexs:
	print (v.ToString())
