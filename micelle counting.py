#set up modules
import numpy as np
import os

#find the length column
header = np.loadtxt (fname="Results.csv", dtype=str, delimiter=",", max_rows=1, unpack = False)
header = header.tolist()
length_col_index = header.index("Length")

#load data
all_data = np.loadtxt(fname="Results.csv", dtype=float, delimiter=",", skiprows=1, usecols = (length_col_index), unpack = True)

#find statistics of the length data
#easy stats first
number_counted = len(all_data)
ln = np.mean(all_data)
ci5 = np.percentile(all_data, 5)
ci95 = np.percentile(all_data, 95)
sd = np.std(all_data)
sdln = sd/ln
#calculate weight average length
length2 = all_data**2
Elength2 = sum(length2)
Elength = sum(all_data)
wn = Elength2/Elength
#calculate the dispersity
pdi = wn/ln

#output data to a text file
dir_name = os.path.relpath(".","..")

f=open("statistics.txt", "w")
f.write("%s \n" % dir_name
        + "number of micelles counted: %d \n" % number_counted
        + "number average length, Ln: %.2f nm \n" % ln
        + "weight average length, Wn: %.2f nm \n" % wn
        + "Wn / Ln (dispersity): %.2f nm \n" % pdi
        + "standard deviation: %.2f nm \n" % sd
        + "standard deviation / Ln: %.2f nm \n" % sdln
        + r"5% confidence interval: " + "%.2f nm \n" % ci5
        + r"95% confidence interval: " + "%.2f nm \n" % ci95
        )
f.close()

#plot the data as a histogram too
