#!/usr/bin/env python

import numpy as np
import pandas as pd
import os

#normalize list to 0,1:
def normalize_list(list):
    list_ar = np.array(list)        
    max_value = np.max(list_ar)
    min_value = np.min(list_ar)
    for x in range(len(list_ar)):
        value = list_ar[x]        
        value = (value - min_value) / (max_value - min_value)        
        list_ar[x]=value          
    return(list_ar)

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


#getting list of files in the current directory
filelist=get_filenames(os.getcwd())

#going to specific file and opening it/ opening Mw results sheet (sheet 3)
arrayed_GPC_curve = []
Timepoint = []
for file in filelist:
    working_sheet = pd.read_excel(f'{file}',sheet_name=3, header=1)    
    #import entire column of data to variable
    arrayed_GPC_curve.append(working_sheet['Mw (g/mol)'])
    dwdlogMw_unnormalised = working_sheet['dW/dLogM']
    #normalize one column using function       
    dwdlogMw_normalised = normalize_list(dwdlogMw_unnormalised)      
    arrayed_GPC_curve.append(dwdlogMw_normalised)
    #create list of timepoints to use as heading     
    Timepoint.append(file)
    Timepoint.append(file)
    

#organising data / create datalist
master_arrayed_GPC_curve = pd.DataFrame(arrayed_GPC_curve, index=Timepoint)
master_arrayed_GPC_curve_T = master_arrayed_GPC_curve.T
master_arrayed_GPC_curve_TS = master_arrayed_GPC_curve_T.sort_index(axis = 1)
master_arrayed_GPC_curve_TS.to_csv('master_arrayed_GPC_curve.csv', na_rep='')

#print(arrayed_GPC_curve)
#print(Mw)
#print(Intensity_normalised)

#this makes sure the cmd window stays open so you can ready any feedback
os.system("pause")