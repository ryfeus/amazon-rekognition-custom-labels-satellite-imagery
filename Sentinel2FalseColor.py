import rasterio
import numpy as np

band8=rasterio.open("B08.jp2")
band4=rasterio.open("B04.jp2")
band3=rasterio.open("B03.jp2")

profile = band8.profile
profile.update({"count": 3, "dtype": "uint8"})

bands = [(band8, 1),(band4, 2),(band3, 3)]

with rasterio.open('false_color.tiff', 'w', **profile) as dest:
	for (band, ind) in bands:
		band_raster = band.read(1).astype(np.float64)/16
		band_raster[band_raster>=255] = 255
		dest.write(band_raster.astype(np.uint8), ind)