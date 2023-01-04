#set up modules
import numpy as np

#find the length column
header = np.loadtxt (fname="results.csv", dtype=str, delimiter=",", max_rows=1, unpack = False)
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
output_array1 = np.array((number_counted, ln, wn))
    # ("Wn / Ln (dispersity)", pdi),
    # ("standard deviation (nm)", sd),
    # ("standard deviation / Ln", sdln),
    # (r"5% confidence interval (nm)", ci5),
    # (r"95% confidence interval (nm)", ci95)
    

output_array2 = np.array((
    "number of micelles counted",
    "number average length (Ln) (nm)",
    "weight average length (Wn) (nm)"))
    # ("Wn / Ln (dispersity)", pdi),
    # ("standard deviation (nm)", sd),
    # ("standard deviation / Ln", sdln),
    # (r"5% confidence interval (nm)", ci5),
    # (r"95% confidence interval (nm)", ci95)
    
    
    
#    "number of micelles counted: %d \r\n" % number_counted
#out2 = "number average length, Ln: %.2f nm \r\n" % ln
#out3 = "weight average length, Wn: %.2f nm \r\n" % wn
# out4 = np.array(("Wn / Ln (dispersity): ", "%.2f" % pdi, " nm"))
# out5 = np.array(("standard deviation: ", "%.2f" % sd, " nm"))
# out6 = np.array(("standard deviation / Ln", "%.2f" % sdln, " nm"))
# out7 = np.array(("5'%'confidence interval: ", "%.2f" % ci5, " nm"))
# out8 = np.array(("95'%'confidence interval: ", "%.2f" % ci95, " nm"))   
#output_array = np.array((out1, out2)) 
                         #out3, out4, out5, out6, out7, out8))

output_headers = list((
     "number of micelles counted",
     "number average length (Ln) (nm)",
     "weight average length (Wn) (nm)",
     "Wn / Ln (dispersity)",
     "standard deviation (nm)",
     "standard deviation / Ln",
     r"5% confidence interval (nm)",
     r"95% confidence interval (nm)"
     ))

np.savetxt('statistics.csv', (output_array1, output_array2), delimiter=",", fmt=("%s, %.2f"), comments="")
#header=str(",".join(output_headers))

#print (output_array)

# print (all_data)
# print (type(all_data))
# print ("%.2f" % ln + " nm")
# print (sd)
# print (ci5)
# print (number_counted)
# print (length2)
# print (wn)
# print (sdln)
# print (pdi)