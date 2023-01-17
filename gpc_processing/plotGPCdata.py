#set up modules
import numpy as np
import matplotlib.pyplot as plt

#import GPC data
def gpc_data_import(filename):
    polymer1 = np.loadtxt(fname=(f'{filename}.csv'), dtype=str, delimiter=',', skiprows=2, unpack="true")
    return(polymer1)


#----run functions on the dataset----
#filename = input('What is the filename of polymer 1? ')
polymer1 = gpc_data_import("P-SS065")
print(polymer1)