#!/usr/bin/env python

import os
import numpy
import pandas


#retrieve a list of .xlsx files from a directory
def get_filenames(directory_in_str):    
    directory = os.fsencode(directory_in_str)
    filelist = []        
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".xlsx"): 
            # print(os.path.join(directory, filename))
            filelist.append(filename)
            continue
        else:
            continue       
    return(filelist)

#get a list of the filenames in folder
directory_in_str = os.getcwd()
#directory_in_str = input('what is the directory you want to examine ')
filelist = get_filenames(directory_in_str)

#list of filenames
#print(filelist)

#going to specific file and opening it/ opening MW results sheet (sheet 2)
Mw_holding = []
filetimes = []
for file in filelist:
    working_sheet = pandas.read_excel(f'{file}',sheet_name=2)
    Mw_holding.append(working_sheet.iloc[8,3])
    filetimes.append(file)



#list of values found
#print(Mw_holding)

#check nummber of values found
#print(len(Mw_holding))

#organising data / create datalist
arrayed_GPC_data = []
arrayed_GPC_data.append(filetimes)
arrayed_GPC_data.append(Mw_holding)
headings = ['Timepoint','Mw']

master_arrayed_GPC_data = pandas.DataFrame(arrayed_GPC_data, index=headings)
#print(arrayed_GPC_data)

# .T means transpose data 
master_arrayed_GPC_data_t = master_arrayed_GPC_data.T

master_arrayed_GPC_data_t.sort_values(by=['Timepoint'])


master_arrayed_GPC_data_t.to_csv('master_arrayed_GPC_data.csv', na_rep='')





#list = [file]


    
# create 2D matrix of values 

os.system("pause")