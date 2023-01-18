#set up modules
import numpy as np
import matplotlib.pyplot as plt

#import GPC data
def gpc_data_import(filename):
    data = np.loadtxt(fname=(f'{filename}.csv'), dtype=str, delimiter=',', skiprows=2, unpack="true")
    mw = data[0]
    WFdLogMW = data[1]
    return(mw, WFdLogMW)


#----run functions on the dataset----

#find out how many datasets
total_samples = int(input('how many samples do you have to plot? '))

#----CEAN UP THE FOLLOWING AND PUT INTO FUNCTIONS:
#1) get sample data
#2) save sample data as text file
#3) plot sample data

#create array to hold all datasets
to_plot = list()

#loop through number of samples appending datasets into array
currentsample = 1

while currentsample <= total_samples:
    fname = input('What is the filename of the next polymer? (do not add extension) ')
    mw, WFdLogMW = gpc_data_import(fname)
    mw = np.ndarray.tolist(mw)
    WFdLogMW = np.ndarray.tolist(WFdLogMW)
    #currentdata = list([mw, WFdLogMW])
    #currentdata = (mw, WFdLogMW)
    #to_plot.append(currentdata)
    #currentsample += 1

    mw = ','.join(mw)
    WFdLogMW = ','.join(WFdLogMW)
    currentdata = list([mw, WFdLogMW])
    to_plot.append(currentdata)
    currentsample += 1

to_plot_2D = np.squeeze(to_plot)
to_plot_2D = np.asarray(to_plot_2D)
to_plot_2D = np.reshape(to_plot_2D, newshape=(2*total_samples, -1))
#print(to_plot_2D)
np.savetxt('arrayed_data.csv', (np.transpose(to_plot_2D)), fmt='%s', delimiter='\n', newline='\n')

   
# addsample = input('Do you have another sample to add? (y/n) ')
# while addsample == 'y':
#     fname_2 = input('What is the filename of polymer 2? ')
#     p2_mw, p2_WFdLogMW = gpc_data_import(fname_2)
#     addsample = input('Do you have another sample to add? (y/n) ')

#plot the data on a graph?


# print(currentdata)