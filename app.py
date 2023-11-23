import numpy as np
import rasterio
import mayavi.mlab as mlab

mlab.figure('elevationn model of assam')
with rasterio.open("./data.tif") as src:
    elev= src.read(1)
nrow, ncol = elev.shape
x,y =np.meshgrid(np.arange(ncol), np.arange(nrow))
z=elev
mesh=mlab.mesh(x,y,z)
mlab.show()

