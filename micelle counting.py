#set up modules
import numpy as np

#find the length column
header = np.loadtxt (fname="results.csv", dtype=str, delimiter=",", max_rows=1, unpack = False)
header = header.tolist()
length_index = header.index("Length")

#print (length_index)
#print (header)
#print (type(header))
#print (length_index)

#load data
all_data = np.loadtxt(fname="Results.csv", dtype=float, delimiter=",", skiprows=1, usecols = (length_index), unpack = True)

print (all_data)
print (type(all_data))

#hello