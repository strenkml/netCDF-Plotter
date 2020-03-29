import xarray as xr
import matplotlib.pyplot as plt

# The input can be any of the Data Variables (Printed when the application starts)
def getData(var):
    d = f[var].sel(latitude=lat, longitude=lon, method='nearest')
    return d

# The input can be any of the Data Variables (Printed when the application starts)
def getDataAndPlot(var):
    d = f[var].sel(latitude=lat, longitude=lon, method='nearest')
    global num_plots
    num_plots += 1
    fig = plt.figure(num_plots)
    fig.suptitle("{} vs time".format(var))
    plt.plot_date(d.coords['time'].data, d.data, ms=1)
    return d

# Relative location of the .nc file to be read
fileName = './G10021-noram-stp-1959-2009.v01r00.nc'

# Latitude and Longitude that is closest to Syracuse (Just off the shore of Oswego)
lat = 43.5
lon = -75.5

# Allows the number of figures to be dynamic
num_plots = 0

f = xr.open_dataset(fileName)
print(f.data_vars)

# Example plots
getDataAndPlot('snowfall')
getDataAndPlot('temperature_max')

# Shows all of the plots
plt.show()
f.close()