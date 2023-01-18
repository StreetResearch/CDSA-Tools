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
        mw = np.ndarray.tolist(mw)
        WFdLogMW = np.ndarray.tolist(WFdLogMW)
        currentdata = list([mw, WFdLogMW])
        to_plot.append(currentdata)
        currentsample += 1
    return(to_plot)

#output the GPC data as a text file
def data_array_to_text(data_array):
    #create pandas dataframe
    s1=pd.Series(data_array[0][0], name='p1 mw')
    s2=pd.Series(data_array[0][1], name='p1 WF')
    s3=pd.Series(data_array[1][0], name='p2 mw')
    s4=pd.Series(data_array[1][1], name='p2 WF')
    df=pd.concat([s1,s2,s3,s4], axis=1)
    #print(df)
    df.to_csv('arrayed_data.csv', index=False, na_rep='')
    
#plot the GPC data as a graph
def plot_GPC_data(arrayed_data):
    #plot graph here          


total_samples = int(input('how many samples do you have to plot? '))
to_plot = compile_GPC_data(total_samples)
data_array_to_text(to_plot)


#----run functions on the dataset----

# #find out how many datasets
# total_samples = int(input('how many samples do you have to plot? '))

# #----CEAN UP THE FOLLOWING AND PUT INTO FUNCTIONS:
# #1) get sample data
# #2) save sample data as text file
# #3) plot sample data
# #use loop and f.write to write file line by line

# #create array to hold all datasets
# to_plot = list()

# #loop through number of samples appending datasets into array
# currentsample = 1

# while currentsample <= total_samples:
#     fname = input('What is the filename of the next polymer? (do not add extension) ')
#     mw, WFdLogMW = gpc_data_import(fname)
#     mw = np.ndarray.tolist(mw)
#     WFdLogMW = np.ndarray.tolist(WFdLogMW)
#     #currentdata = list([mw, WFdLogMW])
#     #currentdata = (mw, WFdLogMW)
#     #to_plot.append(currentdata)
#     #currentsample += 1

#     mw = ','.join(mw)
#     WFdLogMW = ','.join(WFdLogMW)
#     currentdata = list([mw, WFdLogMW])
#     to_plot.append(currentdata)
#     currentsample += 1

# to_plot_2D = np.squeeze(to_plot)
# to_plot_2D = np.asarray(to_plot_2D)
# to_plot_2D = np.reshape(to_plot_2D, newshape=(-1, 2*total_samples))
# #print(to_plot_2D)
# np.savetxt('arrayed_data.csv', (np.transpose(to_plot_2D)), fmt='%s', delimiter='\n', newline='\n')

   
# addsample = input('Do you have another sample to add? (y/n) ')
# while addsample == 'y':
#     fname_2 = input('What is the filename of polymer 2? ')
#     p2_mw, p2_WFdLogMW = gpc_data_import(fname_2)
#     addsample = input('Do you have another sample to add? (y/n) ')

#plot the data on a graph?


# print(currentdata)