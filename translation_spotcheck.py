import netCDF4
import numpy as np
import json

with open('./gridFiles/grid_x99_y99.json') as json_file:
    data = json.load(json_file)

with open('./gridFiles/grid_x55_y11.json') as json_file1:
    data1 = json.load(json_file1)

with open('./gridFiles/grid_x135_y80.json') as json_file2:
    data2 = json.load(json_file2)

miroc2030 = netCDF4.Dataset("./gcmFilesCurvilinear/miroc5_RCP8.5_wyMAX_2020-2049_pchg.nc")

noresm2040 = netCDF4.Dataset("./gcmFilesCurvilinear/noresm1-m_RCP8.5_wyMAX_2030-2059_pchg.nc")

giss2050 = netCDF4.Dataset("./gcmFilesCurvilinear/giss-e2-h_RCP8.5_wyMAX_2040-2069_pchg.nc")

access2060 = netCDF4.Dataset("./gcmFilesCurvilinear/access1.0_RCP8.5_wyMAX_2050-2079_pchg.nc")

csiro2070 = netCDF4.Dataset("./gcmFilesCurvilinear/csiro-mk3.6.0_RCP8.5_wyMAX_2060-2089_pchg.nc")

fgoals2080 = netCDF4.Dataset("./gcmFilesCurvilinear/fgoals-g2_RCP8.5_wyMAX_2070-2099_pchg.nc")


# the durations and return_ints lists below map the values used on the viz to the netCDF indices
# expl: 25-year return interval has netCDF index of 4 as seen at return_ints[3]

durations = [[1, 0], [2, 1], [6, 3], [24, 5], [72, 7]]; 

return_ints = [[2, 0], [5, 1], [10, 2], [25, 4], [50, 5], [100, 6]];



# netCDF files use 0-based indices, so x and y coordinates from gridFile names are -1 below

print('miroc5_RCP8.5_wyMAX_2020-2049')
print(miroc2030["PREC_wyMAX"][0, 0, 98, 98].data == data["2020-2049"]["miroc5_RCP8.5_wyMAX"]["1-hr"]["2-yr"])
print(miroc2030["PREC_wyMAX"][1, 5, 54, 10].data == data1["2020-2049"]["miroc5_RCP8.5_wyMAX"]["2-hr"]["50-yr"])
print(miroc2030["PREC_wyMAX"][3, 4, 134, 79].data == data2["2020-2049"]["miroc5_RCP8.5_wyMAX"]["6-hr"]["25-yr"])

print('noresm1-m_RCP8.5_wyMAX_2030-2059')
print(noresm2040["PREC_wyMAX"][0, 0, 98, 98].data == data["2030-2059"]["noresm1-m_RCP8.5_wyMAX"]["1-hr"]["2-yr"])
print(noresm2040["PREC_wyMAX"][5, 2, 54, 10].data == data1["2030-2059"]["noresm1-m_RCP8.5_wyMAX"]["24-hr"]["10-yr"])
print(noresm2040["PREC_wyMAX"][1, 5, 134, 79].data == data2["2030-2059"]["noresm1-m_RCP8.5_wyMAX"]["2-hr"]["50-yr"])

print('giss-e2-h_RCP8.5_wyMAX_2040-2069')
print(giss2050["PREC_wyMAX"][1, 6, 98, 98].data == data["2040-2069"]["giss-e2-h_RCP8.5_wyMAX"]["2-hr"]["100-yr"])
print(giss2050["PREC_wyMAX"][1, 0, 54, 10].data == data1["2040-2069"]["giss-e2-h_RCP8.5_wyMAX"]["2-hr"]["2-yr"])
print(giss2050["PREC_wyMAX"][3, 5, 134, 79].data == data2["2040-2069"]["giss-e2-h_RCP8.5_wyMAX"]["6-hr"]["50-yr"])

print('access1.0_RCP8.5_wyMAX_2050-2079')
print(access2060["PREC_wyMAX"][0, 0, 98, 98].data == data["2050-2079"]["access1.0_RCP8.5_wyMAX"]["1-hr"]["2-yr"])
print(access2060["PREC_wyMAX"][3, 5, 54, 10].data == data1["2050-2079"]["access1.0_RCP8.5_wyMAX"]["6-hr"]["50-yr"])
print(access2060["PREC_wyMAX"][7, 5, 134, 79].data == data2["2050-2079"]["access1.0_RCP8.5_wyMAX"]["72-hr"]["50-yr"])

print('csiro-mk3.6.0_RCP8.5_wyMAX_2060-2089')
print(csiro2070["PREC_wyMAX"][0, 2, 98, 98].data == data["2060-2089"]["csiro-mk3.6.0_RCP8.5_wyMAX"]["1-hr"]["10-yr"])
print(csiro2070["PREC_wyMAX"][5, 6, 54, 10].data == data1["2060-2089"]["csiro-mk3.6.0_RCP8.5_wyMAX"]["24-hr"]["100-yr"])
print(csiro2070["PREC_wyMAX"][1, 5, 134, 79].data == data2["2060-2089"]["csiro-mk3.6.0_RCP8.5_wyMAX"]["2-hr"]["50-yr"])

print('fgoals-g2_RCP8.5_wyMAX_2070-2099_pchg.nc')
print(fgoals2080["PREC_wyMAX"][7, 2, 98, 98].data == data["2070-2099"]["fgoals-g2_RCP8.5_wyMAX"]["72-hr"]["10-yr"])
print(fgoals2080["PREC_wyMAX"][5, 0, 54, 10].data == data1["2070-2099"]["fgoals-g2_RCP8.5_wyMAX"]["24-hr"]["2-yr"])
print(fgoals2080["PREC_wyMAX"][1, 4, 134, 79].data == data2["2070-2099"]["fgoals-g2_RCP8.5_wyMAX"]["2-hr"]["25-yr"])










