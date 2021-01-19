
import netCDF4
import numpy as np
import json
import os
import csv
import caffeine 

def decadeDataSets():
    ds_dict = {}

    gcm_list = [
        "access1.0_RCP8.5_wyMAX",
        "access1.3_RCP8.5_wyMAX",
        "bcc-csm1.1_RCP8.5_wyMAX",
        "canesm2_RCP8.5_wyMAX",
        "ccsm4_RCP8.5_wyMAX",
        "csiro-mk3.6.0_RCP8.5_wyMAX",
        "ensemble_RCP8.5_wyMAX",
        "fgoals-g2_RCP8.5_wyMAX",
        "gfdl-cm3_RCP8.5_wyMAX",
        "giss-e2-h_RCP8.5_wyMAX",
        "miroc5_RCP8.5_wyMAX",
        "mri-cgcm3_RCP8.5_wyMAX",
        "noresm1-m_RCP8.5_wyMAX"
    ]


    decade_list = [ #edit based on decades in NetCDF data
        "2020-2049",
        "2030-2059",
        "2040-2069",
        "2050-2079",
        "2060-2089",
        "2070-2099"
    ]

    for dec in decade_list:
        ds_dict[dec] = {}

        for gcmodel in gcm_list:
            ds_dict[dec][gcmodel] = netCDF4.Dataset("./gcmFilesCurvilinear/" + gcmodel + "_{}_pchg.nc".format(dec))


    return ds_dict   

         

def gcmDecadeDataMap(gcmDataSet, x, y): 
    #first element is duration in hours, second element is the first element's index in the NetCDF PREC_wyMAX array 
    durations = [[1, 0], [2, 1], [6, 3], [24, 5], [72, 7]]; 
    #first element is return int in years, second element is the first element's index in the NetCDF PREC_wyMAX array 
    return_ints = [[2, 0], [5, 1], [10, 2], [25, 4], [50, 5], [100, 6]];

    precip_data = {}

    for d in durations:
        duration_label = '{}-hr'.format(d[0]);
        precip_data[duration_label] = {};

        for r in return_ints:
            return_label = '{}-yr'.format(r[0]);
            data = gcmDataSet['PREC_wyMAX'][d[1], r[1], x, y].data;
            precip_data[duration_label][return_label] = float(data);

    return precip_data;



def writeJSON(x, y):

    ds_dictionary = decadeDataSets()

    gcmList = [
        "access1.0_RCP8.5_wyMAX",
        "access1.3_RCP8.5_wyMAX",
        "bcc-csm1.1_RCP8.5_wyMAX",
        "canesm2_RCP8.5_wyMAX",
        "ccsm4_RCP8.5_wyMAX",
        "csiro-mk3.6.0_RCP8.5_wyMAX",
        "ensemble_RCP8.5_wyMAX",
        "fgoals-g2_RCP8.5_wyMAX",
        "gfdl-cm3_RCP8.5_wyMAX",
        "giss-e2-h_RCP8.5_wyMAX",
        "miroc5_RCP8.5_wyMAX",
        "mri-cgcm3_RCP8.5_wyMAX",
        "noresm1-m_RCP8.5_wyMAX"
    ]


    decadeList = [ #edit based on decades in NetCDF data
        "2020-2049",
        "2030-2059",
        "2040-2069",
        "2050-2079",
        "2060-2089",
        "2070-2099"
    ]

    grid_dict = {}

    file_name = "./gridFiles/grid_x{}_y{}.json".format(x, y)

    for decade in decadeList:
        grid_dict[decade] = {}

        for gcm in gcmList: 

            ds = ds_dictionary[decade][gcm]
            xIndex = int(x) - 1
            yIndex = int(y) - 1
            grid_dict[decade][gcm] = gcmDecadeDataMap(ds, xIndex, yIndex)

    with open(file_name, "w") as outfile: 
        json.dump(grid_dict, outfile)


# open grid csv, loop over rows to write JSON files

filename = "./WRF_12km_LUT_cropped_NoOcean.csv"

fields = [] 
rows = [] 

with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    #['Center Lat', 'Min Lat', 'Max Lat', 'Center Lon', 'Min Lon', 'Max Lon', 'row index (1-based)', 'column index (1-based)']
    fields = next(csvreader) 

    for row in csvreader: 
        rows.append(row)

    for grid in rows:
        writeJSON(grid[7] , grid[6])





# https://www.google.com/url?hl=en&q=https://www.mathworks.com/help/matlab/ref/griddata.html&sa=D&ust=1604601191388000&usg=AFQjCNH6j7XGYBwt9StID6EM8hiFtMHU1w

