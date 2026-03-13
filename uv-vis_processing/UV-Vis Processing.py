#!/usr/bin/env python

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#get list of files in directory

#get a list of the filenames
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

#Import UV-Vis data
def import_UV_Vis_Data(filename_ext):
    UV_Data = pd.read_csv(f'{filename_ext}', sep=',', header=[0,1])
    sample_names = list(UV_Data.columns)
    return(UV_Data, sample_names)

#import data from all .csv files in directory
def import_all_UV_Data(filelist_csv_ext, directory):
    All_UV_Data = []
    All_sample_names = []
    for x in filelist_csv_ext:
        Current_UV_Data, Current_sample_names = import_UV_Vis_Data(x)
        print(f'The UV-Vis Data for {filelist_csv_ext} is:')
        print(Current_UV_Data)
        All_UV_Data.append(Current_UV_Data)
        All_sample_names.extend(Current_sample_names)
    All_UV_Data = pd.concat(All_UV_Data, axis=1)
    print(f'The master UV-Vis Data Table is:')
    print(All_UV_Data)
    print('The samples in this dataset are:')
    print(All_sample_names)
    #create a subfolder to save data
    try:
        os.mkdir('Results') #creating a subfolder
    except FileExistsError: #if subfolder already exists
        pass 
    #save 3D data as table
    All_UV_Data.to_excel('Results/Aggregated UV-Vis Data.xlsx')
    All_UV_Data.to_csv('Results/Aggregated UV-Vis Data.csv', sep=',', index=True)
    print(f'All datasets in {directory} have been successfully saved to a joint file')
    return(All_UV_Data, All_sample_names)

#plot UV spectrum for each sample from an array of compiled XY datasets
def plot_UV_spectrum(arrayed_UV_Data, sample_names):
    i = 0
    while i < len(sample_names):        
        filename = sample_names[i]
        print(f'plotting UV spectrum for {filename}')
        fig, ax = plt.subplots(figsize=(10, 10))
        plt.plot(arrayed_UV_Data[i][0],arrayed_UV_Data[i][1])
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Absorbance')
        plt.savefig(f'Results/{filename}_UV-Spectrum.png', dpi=600, transparent=True)
        plt.close()
        print(f'UV spectrum for {filename}nm successfully plotted')
        i+=1
    print('All UV spectra successfully plotted bud.')

#plot a UV-Vis spectrum
def extract_plot_UV_spectrum(UV_Data):
    #print(UV_Data)
    #get the number of samples to process
    no_of_columns = UV_Data.shape[1]
    no_of_samples = int(no_of_columns/2)
    print(f'there are {no_of_samples} samples in this dataset to process')      

    #extract the individual XY datasets from the master array  
    Compiled_UV_Datasets = []
    sample_names = []  
    i=0
    while i < no_of_samples:
        sample_name = UV_Data.columns[2*i]
        sample_name = sample_name[0]        
        print(f'compiling UV dataset for {sample_name}.')
        xindex_loc = int(2*i)
        yindex_loc = int((2*i)+1)
        print(f'this dataset is in column {xindex_loc} and {yindex_loc}')
        current_UV_trace = []
        current_UV_trace_x = UV_Data.iloc[:, xindex_loc]
        current_UV_trace_x.name = f'{sample_name}-wavelength'
        current_UV_trace_y = UV_Data.iloc[:, yindex_loc]
        current_UV_trace_y.name = f'{sample_name}-absorbance'
        current_UV_trace.append(np.array(current_UV_trace_x))
        current_UV_trace.append(np.array(current_UV_trace_y))
        current_UV_trace_pd = pd.DataFrame(current_UV_trace)
        current_UV_trace_pd = current_UV_trace_pd.T
        current_UV_trace_pd.to_excel(f'Results/{sample_name}_UV_Spectrum.xlsx')
        current_UV_trace_pd.to_csv(f'Results/{sample_name}_UV_Spectrum.csv', sep=',', index=True)
        Compiled_UV_Datasets.append(current_UV_trace)
        sample_names.append(sample_name)
        #print('--------------')
        #print('The current dataset is: ')
        #print(current_UV_trace)
        i+=1     
    #print(Compiled_UV_Datasets)
    #print(type(Compiled_UV_Datasets))
    #print(sample_names)
    plot_UV_spectrum(Compiled_UV_Datasets, sample_names)    
    return(Compiled_UV_Datasets, sample_names)
        
#Extract absorbance at a specific wavelength
def extract_UV_absorbance_at_specifc_wavelength(compiled_UV_data, sample_names, wavelength):
    i=0
    absorbance_values = []    
    while i < len(sample_names):
        print(f'Extracting absorbance at {wavelength}nm for {sample_names[i]}')
        current_UV_spectrum = pd.DataFrame(compiled_UV_data[i][1], index=compiled_UV_data[i][0])
        #print(current_UV_spectrum)
        #current_UV_spectrum.to_excel('285nmtest.xlsx')
        current_absorbance = current_UV_spectrum.loc[wavelength]
        absorbance_values.append(current_absorbance)
        print(f'The absorbance at {wavelength}nm for {sample_names[i]} is {current_absorbance[0]}')
        i+=1
    master_absorbance_values = pd.DataFrame(absorbance_values, index=sample_names)
    master_absorbance_values = master_absorbance_values.rename(columns={0:f'{wavelength}nm'})
    print(f'The following absorbance values were found at {wavelength}nm for the current working directory')
    print(master_absorbance_values)
    master_absorbance_values.to_excel(f'Results/Arrayed_Absorbance_Data_{wavelength}nm.xlsx')
    master_absorbance_values.to_csv(f'Results/Arrayed_Absorbance_Data_{wavelength}nm.csv', sep=',', index=True)
    return(master_absorbance_values)        

        



#-----------------------


#get current directory
directory_in_str = os.getcwd()
fileformat = '.csv'
#get a list of .csv files in the current directory
filelist_csv_noext, filelist_csv_ext = get_filenames(directory_in_str, f'{fileformat}')
#inform the user of the current directory and .csvf files within
print(f'The working folder is: \n {directory_in_str}')
print('-------')
print(f'The following {fileformat} files are in the working folder: \n {filelist_csv_ext}')
print('-------')

#import the UV-Vis data
all_UV_Data, all_sample_names = import_all_UV_Data(filelist_csv_ext, directory_in_str)
#extract and plot individual UV traces

#print(All_UV_Data)
print('-------')
compiled_UV_data, sample_names = extract_plot_UV_spectrum(all_UV_Data)

#Extract absorbance at specific wavelengths from each dataset, ie 285nm
print('-------')
all_extraced_wavelengths = []
#285nm
wavelength_to_extract = 285
absorbance_285 = extract_UV_absorbance_at_specifc_wavelength(compiled_UV_data, sample_names, wavelength_to_extract)
all_extraced_wavelengths.append(wavelength_to_extract)
master_extracted_UV_absorbances = absorbance_285
print('-------')
#260nm
wavelength_to_extract = 260
absorbance_260 = extract_UV_absorbance_at_specifc_wavelength(compiled_UV_data, sample_names, wavelength_to_extract)
all_extraced_wavelengths.append(wavelength_to_extract)
master_extracted_UV_absorbances = master_extracted_UV_absorbances.join(absorbance_260, how='left')
print('-------')
#240nm
wavelength_to_extract = 240
absorbance_240 = extract_UV_absorbance_at_specifc_wavelength(compiled_UV_data, sample_names, wavelength_to_extract)
all_extraced_wavelengths.append(wavelength_to_extract)
master_extracted_UV_absorbances = master_extracted_UV_absorbances.join(absorbance_240, how='left')
#output a table of all of the UV absorbances together
print('-------')
master_extracted_UV_absorbances.to_excel(f'Results/Master_Arrayed_Absorbance_Data.xlsx')
master_extracted_UV_absorbances.to_csv(f'Results/Master_Arrayed_Absorbance_Data.csv', sep=',', index=True)
print('The master table of extraced abosrbance values is as follows: ')
print(master_extracted_UV_absorbances)
print('-------')


#Complete
print('Data processing complete for all UV-Vis samples in this folder.')
print('We\'re all done here bud, you have yourself a nice day there.')
os.system("pause")


#FUTURE
#save logs to file
#plot and crop UV spectra to 200-350nm





