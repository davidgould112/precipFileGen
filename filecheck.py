import os
import csv 

directory = "./gridFiles/"

file_dict = {}
file_list = os.listdir(directory)
for filename in file_list:
	file_dict[filename] = True;

print(len(file_list));
csvFile = "./WRF_12km_LUT_cropped_NoOcean.csv"

fields = [] 
rows = [] 

with open(csvFile, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    #['Center Lat', 'Min Lat', 'Max Lat', 'Center Lon', 'Min Lon', 'Max Lon', 'row index (1-based)', 'column index (1-based)']
    fields = next(csvreader) 

    for row in csvreader: 
        rows.append(row)

    print(len(rows));
    for grid in rows:
        file_name = "grid_x{}_y{}.json".format(grid[7], grid[6])
        if file_dict[file_name] == True:
        	del file_dict[file_name];
        

    
    print(file_dict)


