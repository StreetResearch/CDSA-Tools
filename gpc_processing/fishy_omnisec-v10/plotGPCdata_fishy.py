#set up modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import GPC data
def gpc_data_import(filename):
    data = np.loadtxt(fname=(f'{filename}.csv'), dtype=str, delimiter=',', skiprows=2, unpack="true")
    mw = data[0]
    WFdLogMW = data[1]
    return(mw, WFdLogMW)

#Compile all GPC data
def compile_GPC_data(total_samples):
    #create array to hold all datasets
    to_plot = list()

    #loop through number of samples appending datasets into array
    currentsample = 1

    while currentsample <= total_samples:
        fname = input('What is the filename of the next polymer? (do not add extension) ')
        mw, WFdLogMW = gpc_data_import(fname)
        WFdLogMW = WFdLogMW.astype(float)
        mw = np.ndarray.tolist(mw)
        WFdLogMW = np.ndarray.tolist(WFdLogMW)
        #normalize WFdLogMw
        norm_WFdLogMW = (WFdLogMW-np.min(WFdLogMW))/(np.max(WFdLogMW)-np.min(WFdLogMW))
        currentdata = list([mw, norm_WFdLogMW])
        to_plot.append(currentdata)
        currentsample += 1
    return(to_plot)

#output the GPC data as a text file
def data_array_to_text(data_array, no_of_samples):
    #can add in if statements for multiple samples with while loops that have i,j as indices, start at 0 and increase to max? also name varaibles,
    #create pandas dataframe
    s1=pd.Series(data_array[0][0], name='p1 mw')
    s2=pd.Series(data_array[0][1], name='p1 WF')
    if no_of_samples > 1:
        s3=pd.Series(data_array[1][0], name='p2 mw')
        s4=pd.Series(data_array[1][1], name='p2 WF')
        df=pd.concat([s1,s2,s3,s4], axis=1)
    if no_of_samples > 2:
        s5=pd.Series(data_array[2][0], name='p3 mw')
        s6=pd.Series(data_array[2][1], name='p3 WF')
        df=pd.concat([s1,s2,s3,s4,s5,s6], axis=1)
    if no_of_samples == 1:
        df=pd.concat([s1,s2], axis=1)
    #print(df)
    df.to_csv('arrayed_data.csv', index=False, na_rep='')
    
#plot the GPC data as a graph
def plot_GPC_data(arrayed_data, no_of_samples):
    #sort datasets out
    dataset1 = np.array(arrayed_data[0], dtype=float)
    if no_of_samples > 1:
        dataset2 = np.array(arrayed_data[1], dtype=float)
    if no_of_samples > 2:
        dataset3 = np.array(arrayed_data[2], dtype=float)    
    plt.rc('font', size=8)
    
    #configure and plot graph
    fig, ax = plt.subplots(figsize=(6.4,4.8), dpi=1200, layout='constrained')
    ax.plot(dataset1[0], dataset1[1], 'k', label='PFTMC$_{16}$-$\it{b}$-PDMAEMA$_{131}$', linewidth=2)
    if no_of_samples > 1:
        ax.plot(dataset2[0], dataset2[1], 'r', label='BD-PFTMC$_{16}$-$\it{b}$-PDMAEMA$_{112}$', linewidth=2)
    if no_of_samples > 2:
        ax.plot(dataset3[0], dataset3[1], 'c', label='Block$_{1}$-$\it{b}$-Block$_{2}$', linewidth=2)
    ax.set_xlabel('Molecular Weight (Da)')
    ax.set_ylabel('Normalized WF/dLogMw')
    ax.set_xscale('log')
    ax.set_xlim(left=1, right=10000000000)
    ax.set_ylim(bottom=0, top=1)
    ax.set_xticks((1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,1000000000,10000000000))
    ax.set_yticks((0,0.2,0.4,0.6,0.8,1.0,1.2))
    ax.legend()
    plt.savefig('combined_GPC_plot.png')
    #plt.show()
            

#----run functions on the dataset----
#find out how many datasets
total_samples = int(input('how many samples do you have to plot? '))
#process the data
to_plot = compile_GPC_data(total_samples)
data_array_to_text(to_plot, total_samples)
plot_GPC_data(to_plot, total_samples)

#@TO DO
#for future - use loops and dictionary to plot and save to files an unlimited numbers of datasets!
#https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
