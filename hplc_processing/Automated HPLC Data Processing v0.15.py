#!/usr/bin/env python

import os
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from scipy.signal import find_peaks
from hplc.io import load_chromatogram
from hplc.quant import Chromatogram
from colorama import Fore, Back, Style, init

#load the 3D data from the csv file as a dataframe
def load_HPLC_3D_Data (filename):
    print(f'\033[31m Now Processing {filename}. Hold Tight!\n')
    data = pd.read_csv(f'{filename}.csv', sep=',', header=78, index_col=0)
    column_headings = list(data.columns)
    column_headings_nm = []
    for x in column_headings:
        x = x[:3] + '.' + x[3:]
        column_headings_nm.append(x)
    data.columns = column_headings_nm
    #transpose dataframe so Tr is x axis
    data_T = data.T

    #Replace column heading (x axis) with shortened values
    column_headings_T = list(data_T.columns)
    column_headings_T_min = []
    for x in column_headings_T:
        x = round(x, 2)
        column_headings_T_min.append(x)
    data_T.columns = column_headings_T_min
    print(f'\033[0m Loaded PDA Data for {filename} successfully')
    return(data, data_T)

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

#extract HPLC traces from dataframe
def extract_HPLC_trace(dataframe, wavelength, filename):
    HPLC_trace_wavelength = dataframe[wavelength]
    HPLC_trace_wavelength.rename_axis(index='Tr', inplace=True)
    print(f'HPLC Chromatogram at {wavelength}nm successfully extracted')
    HPLC_trace_wavelength.rename(f'{filename}_{wavelength}nm')
    HPLC_trace_wavelength.to_excel(f'{filename}/{filename}_Chromatogram_{wavelength}nm.xlsx')
    HPLC_trace_wavelength.to_csv(f'{filename}/{filename}_Chromatogram_{wavelength}nm.csv', sep=',', index=True)
    print(f'Chromatogram for UV signal at {wavelength}nm data successfully saved')
    return(HPLC_trace_wavelength) 

#plot and save a chromatogram at the specified wavelength
def plot_HPLC_Chromatogram (HPLC_trace_wavelength, wavelength, filename):
    #create the plot and specify the size
    fig, ax = plt.subplots(figsize=(15, 5))
    #modify the axis to be nice - create x and y axis labels
    #yticks = np.linspace(200, 400, 5)
    #xticks = [0,5,10,15,20,25,30,35,40,45,50,55,60]
    #plot the graph
    plt.plot(HPLC_trace_wavelength)
    #plt.xticks(xticks)
    #plt.yticks(yticks)
    plt.xlabel('Retention Time (min)')
    plt.ylabel('Absorbance')
    plt.savefig(f'{filename}/{filename}_Chromatogram_{wavelength}nm.png', dpi=600, transparent=True)
    plt.close()
    print(f'Chromatogram for UV signal at {wavelength}nm successfully plotted')
    #plt.show()

#plot UV spectrum for a specific peak
def plot_UV_spectrum(UV_trace, UV_wavelengths, filename, peak_name):
    xticks = np.linspace(200, 400, 5)
    fig, ax = plt.subplots(figsize=(10, 10))
    UV_wavelengths = np.array(UV_wavelengths, dtype=np.float32)
    plt.plot(UV_wavelengths, UV_trace)
    plt.xticks(ticks=xticks, labels=xticks)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Absorbance')
    plt.savefig(f'{filename}/{filename}_285nm_Tr{peak_name}_UV-spectrum.png', dpi=600, transparent=True)
    plt.close()
    print(f'UV Spectrum for peak at Tr={peak_name} successfully plotted')
    return()


#find peaks from HPLC trace
def pick_chromatogram_peaks(HPLC_Trace, UV_wavelength, filename):
    peak_integer_index, peak_properties = find_peaks(HPLC_Trace, threshold=(70, None))
    #print(peak_integer_index)
    #Extract retention time from peak index
    peak_retention_time = []
    peak_maxima = []
    for x in peak_integer_index:
        peak_retention_time.append(HPLC_Trace.index[x])
        peak_maxima.append(HPLC_Trace.iloc[x])
    print('Peaks were detected at the following retention times:')
    print(peak_retention_time)
    print('These peaks had the following maxima:')
    print(peak_maxima)
    print('-------')
    #plot chromatogram with picked peaks labeled
    fig, ax = plt.subplots(figsize=(15, 5))
    plt.plot(HPLC_Trace)
    plt.plot(peak_retention_time, peak_maxima, "x")
    plt.xlabel('Retention Time (min)')
    plt.ylabel('Absorbance')
    plt.savefig(f'{filename}/{filename}_Chromatogram_{UV_wavelength}nm_Peaks-Picked.png', dpi=600, transparent=True)
    plt.close()
    #plt.show()
    return(peak_integer_index, peak_retention_time, peak_maxima)

#extract and plot UV spectrum from major peaks
def extract_plot_UV_spectrum(Loaded_HPLC_Data, Loaded_HPLC_Data_T, peak_retention_time, filename):
    #extract and plot the UV spectrum of each peak
    #crop peaks to 2dp so they match UV column headings
    peak_retention_time_min = []
    for x in peak_retention_time:
        x = round(x, 2)
        peak_retention_time_min.append(x)
    #extract the UV spectrum of each peak and plot as a graph
    UV_spectra_table = []
    UV_spectra_wavelengths = list(Loaded_HPLC_Data.columns)
    print(f'The PDA signal ranges from {UV_spectra_wavelengths[0]}nm to {UV_spectra_wavelengths[-1]}nm')
    for x in peak_retention_time_min:
        UV_spectra_table.append(list(Loaded_HPLC_Data_T[x]))
        plot_UV_spectrum(Loaded_HPLC_Data_T[x], UV_spectra_wavelengths, filename, x)
    #Output these arrayed UV spectra as a data table
    UV_spectra_table = pd.DataFrame(UV_spectra_table)
    UV_spectra_table = UV_spectra_table.T
    UV_spectra_table.columns=peak_retention_time_min
    UV_spectra_table.index=UV_spectra_wavelengths
    print('-------')
    print('The detected peaks and associated UV spectra are as follows:')
    print(UV_spectra_table)
    UV_spectra_table.to_excel(f'{filename}/{filename}_Arrayed_Peak_UV_Spectra.xlsx')
    UV_spectra_table.to_csv(f'{filename}/{filename}_Arrayed_Peak_UV_Spectra.csv', sep=',', index=True)
    return(UV_spectra_table)

#process HPLC chromatogram using hplc-py
#load chromatogram
def hplc_py_processing(wavelength, filename):
    print(f'HPLC-py processing for {filename} at {wavelength}nm in progress...')
    loaded_chromatogram = load_chromatogram(f'{filename}/{filename}_Chromatogram_{wavelength}nm.csv', cols={'Tr':'time', f'{wavelength}': 'signal'})
    #convert to chromatogram object
    chrom = Chromatogram(loaded_chromatogram)
    #correct baseline
    chrom.correct_baseline(window=3)
    #fit peaks
    peaks = None
    try:
        peaks = chrom.fit_peaks(buffer=50, prominence=0.02)
    except ValueError:
        print(f'Ohh dear bud, looks like HPLC-py cannot detect the peaks in {filename} at {wavelength}nm. Trying agan with looser parameter bounds... This might take a while, why not head to Timmy\'s?')
        try:
            peaks = chrom.fit_peaks(buffer=50, prominence=0.02, param_bounds={'amplitude':[0.001, 100], 'scale':[0, np.inf]})
        except ValueError:
            print('nope, HPLC-py just doesn\'t like this trace. Giving up until someone smarter can fix my code...')      
    print('The detected peaks and integrations are as follows:')
    print(peaks)
    print('-------')
    #save the data
    try:
        peaks.to_excel(f'{filename}/{filename}_HPLC-py_Fitted-Peaks_{wavelength}nm.xlsx')
        peaks.to_csv(f'{filename}/{filename}_HPLC-py_Fitted-Peaks_{wavelength}nm.csv', sep=',', index=True)
    except AttributeError:
        pass

    #save chromatogram
    fig, ax = chrom.show()
    ax.legend()
    plt.savefig(f'{filename}/{filename}_HPLC-py_Chromatogram_Fitted_{wavelength}nm.png', dpi=600, transparent=False)
    plt.close()
    plt.style.use('default')
    print(f'HPLC-py processing complete for {filename}.')
    print('-------')
    return(peaks)

#Process all .csv files in the current directory
def process_HPLC_data_from_filelist(filelist):
    #load a HPLC dataset
    for x in filelist:
        filename = x
        Loaded_HPLC_Data, Loaded_HPLC_Data_T = load_HPLC_3D_Data(filename)
        #create a subfolder to save data
        try:
            os.mkdir(f'{filename}') #creating a subfolder
        except FileExistsError: #if subfolder already exists
            pass 
        #save 3D data as table
        Loaded_HPLC_Data_T.to_excel(f'{filename}/{filename}_PDA_Data.xlsx')
        Loaded_HPLC_Data_T.to_csv(f'{filename}/{filename}_PDA_Data.csv', sep=',', index=True)
        # #print(Loaded_HPLC_Data)
        # #print(list(Loaded_HPLC_Data.columns))
        #-----------------------

        #plot and save a 2D heatmap of the 3D PDA signal
        #create the plot and specify the size
        fig, ax = plt.subplots(figsize=(15, 5))
        #modify the axis to be nice - create x and y axis labels
        yticks = np.linspace(200, 400, 5)
        xticks = [0,5,10,15,20,25,30]
        #plot the graph
        plt.imshow(Loaded_HPLC_Data_T, cmap='viridis', interpolation='nearest', extent=[0,30,400,200], aspect=0.1)
        plt.xticks(xticks)
        plt.yticks(yticks)
        plt.xlabel('Retention Time (min)')
        plt.ylabel('Wavelength (nm)')
        plt.savefig(f'{filename}/{filename}_PDA-Plot.png', dpi=600, transparent=True)
        plt.close()
        print('2D heatmap of the 3D PDA Data successfully plotted')
        print('-------')
        #plt.show()
        #-----------------------

        #Extract and plot the chromatogram from specific wavelengths
        #Extract the chromatogram from specific wavelengths
        wavelength_to_plot_1 = '284.75'
        Trace_285nm = extract_HPLC_trace(Loaded_HPLC_Data, wavelength_to_plot_1, filename)
        plot_HPLC_Chromatogram (Trace_285nm, wavelength_to_plot_1, filename)
        wavelength_to_plot_2 = '259.63'
        Trace_260nm = extract_HPLC_trace(Loaded_HPLC_Data, wavelength_to_plot_2, filename)
        plot_HPLC_Chromatogram (Trace_260nm, wavelength_to_plot_2, filename)
        print('-------')
        #-----------------------

        #extract and plot UV spectrum from major peaks
        #find peaks from HPLC trace
        peak_integer_index, peak_retention_time, peak_maxima = pick_chromatogram_peaks(Trace_285nm, wavelength_to_plot_1, filename)
        UV_spectra_table = extract_plot_UV_spectrum(Loaded_HPLC_Data, Loaded_HPLC_Data_T, peak_retention_time, filename)
        print('-------')
        #-----------------------

        #process HPLC chromatogram at 285nm and 260nm using hplc-py
        try:
            HPLCpy_Peaks_1 = hplc_py_processing(wavelength_to_plot_1, filename)                   
        except ValueError:
            print(f'Sorry pal, HPLC-py did not like {filename} at {wavelength_to_plot_1}nm. The chromatogram trace shape is not compatible with HPLC-py.')
        try:
            HPLCpy_Peaks_2 = hplc_py_processing(wavelength_to_plot_2, filename)        
        except ValueError:
            print(f'Sorry pal, HPLC-py did not like {filename} at {wavelength_to_plot_2}nm. The chromatogram trace shape is not compatible with HPLC-py.')
        
        #sample complete
        print(f'Data processing complete for {filename}. HOORAY!! =)')
        continue


#-----------------------


#get a list of the filenames
directory_in_str = os.getcwd()
fileformat = '.csv'
#get a list of .csv files in the current directory
filelist_csv_noext, filelist_csv_ext = get_filenames(directory_in_str, f'{fileformat}')

#inform the user of the current directory and .csvf files within
print(f'The working folder is: \n {directory_in_str}')
print('-------')
print(f'The following {fileformat} files are in the working folder: \n {filelist_csv_ext}')
print('-------')
#-----------------------

#Process all .csv files in the current directory
process_HPLC_data_from_filelist(filelist_csv_noext)



#FUTURE
#calculate total area of peaks and % yield of each product
#HPLCpy_total_peak_area = HPLCpy_Peaks['retention_time', 'area']

#Complete
print('Data processing complete for all HPLC samples in this folder. Have a nice day buddy!')
os.system("pause")








#TESTS

#check the dataframe has loaded correctly
    #print(filename)
    #print(Loaded_HPLC_Data.head(0))
    #print(Loaded_HPLC_Data.info())
    #print(Loaded_HPLC_Data)



#TO DO
#make line graph beautiful
#adjust font sizes for 2D plot
#get HPLC-py scores functonality working
#enable the ability to get % conversion from HPLC chromatogram
#auto detect UV range and run time for each sample
#fix HPLC-py peak detection
#Plot UV peaks cropped to specific wavelength(200-300)