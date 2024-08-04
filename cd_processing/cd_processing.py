import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#retrieve a list of .csv files from a directory
def get_filenames(directory_in_str, filetype):    
    directory = os.fsencode(directory_in_str)
    filelist = []
    filelist_with_extensions = []        
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(filetype): 
            # print(os.path.join(directory, filename))
            filelist_with_extensions.append(filename)
            filename_noext = os.path.splitext(filename)[0]
            filelist.append(filename_noext)
            continue
        else:
            continue       
    return(filelist, filelist_with_extensions)

def load_cd_data(filename):
    CD_Data = pd.read_csv(filename, sep='\t', header=19, names=('wavelength', filename, 'Absorbance'))
    CD_Data.drop(CD_Data.tail(34).index,inplace=True) #drop last n rows
    return(CD_Data)
    
#get a list of the filenames
directory_in_str = os.getcwd()
fileformat = '.txt'
#get a list of .csv files in the current directory
filelist_csv_noext, filelist_csv_ext = get_filenames(directory_in_str, f'{fileformat}')

#inform the user of the current directory and .csvf files within
print(f'The working folder is: \n {directory_in_str}')
print('-------')
print(f'The following {fileformat} files are in the working folder: \n {filelist_csv_ext}')
print('-------')
#-----------------------

#load CD data
Master_CD_Data = []
for x in filelist_csv_ext:
    CD_Data = load_cd_data(x)
    #extract CD trace
    ###FIX THISTO EXTRACT A COLUMN
    Wavelength = CD_Data.iloc[0]
    CD_signal = CD_Data.iloc[1]
    CD_signal.rename(f'{x}')
    Master_CD_Data.append(Wavelength)
    Master_CD_Data.append(CD_signal)
print(CD_Data)
print(Wavelength)
print(CD_signal)