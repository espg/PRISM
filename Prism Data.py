# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas
from scipy import io
import scipy
from scipy import spatial as SP

# <codecell>

# Define according to local location
climate_file = io.netcdf.netcdf_file('C:\Users\matthews\Dropbox\PRISM data\monthly.nc')

# <codecell>

# Viewing the file attributes
print(climate_file.variables)
print(climate_file.variables['lat'][0])  # First element of 'lat'
print(len(climate_file.variables['lat'][:]))
climate_file.dimensions

# <codecell>

# Variables that we care about
temp_min = climate_file.variables['temp_min']
temp_max = climate_file.variables['temp_max']
precip_mean = climate_file.variables['precip_mean']
lon = climate_file.variables['lon']
lat = climate_file.variables['lat']

# <codecell>

# Do the below for temp_min, temp_max, and precip
indexed_temp_min = pandas.Panel(temp_min[:,:,:],items=pandas.date_range('1/1/1895',periods=1403,freq='M'),major_axis=lat[:],minor_axis=lon[:])
stacked = indexed_temp_min.to_frame()

# <codecell>

stacked.ix[(lat[120],lon[120]),'1999'].plot()

# <codecell>


