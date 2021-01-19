import xesmf as xe
import xarray as xr
import netCDF4
import os
import numpy as np

lonmin = -131.3447
lonmax = -105.18347
latmin = 38.32287
latmax = 51.482388

res= 1/16	

# for filename in range(os.listdir('./gcmFilesCurvilinear/'):


grid = xe.util.grid_2d(lonmin-res/2, lonmax+res/2, res, latmin-res/2, latmax+res/2, res)

# grid = xr.Dataset({'lat': (['lat'], np.arange(latmin, latmax, 1.0)),
                   #   'lon': (['lon'], np.arange(lonmin, lonmax, 1.5)),
                   #  }
                   # )

ds = xr.open_dataset('./gcmFilesCurvilinear/ensemble_RCP8.5_wyMAX_2020-2049_pchg.nc')

dr = ds['PREC_wyMAX']

rgr = xe.Regridder(ds, grid, method='bilinear')

dr_out = rgr(dr)
# print("DR OUT")
# print(dr_out)

dr_out.to_netcdf("./gcmFilesRectilinear/" + "ensemble_RCP8.5_wyMAX_2020-2049_pchg_16th.nc", "w", "NETCDF4")



# dist = ((lats - lat)**2 + (lons-lon)**2)**0.5
# x,y = np.unravel_index(np.argmin(dist, axis=None), dist.shape)