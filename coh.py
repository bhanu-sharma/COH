import numpy as np

# Set up matplotlib and use a nicer set of plot parameters
import matplotlib
import matplotlib.pyplot as plt

from astropy.io import fits
image_file = fits.open("SPITZER_I2_46466816_0000_0000_2_bcd.fits")

image_data = fits.getdata(image_file)
print(type(image_data))
print(image_data.shape)

plt.imshow(image_data, cmap='gray')
plt.colorbar()

# To see more color maps
# http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
