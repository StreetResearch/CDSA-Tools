#set up modules
import numpy as np
import os
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

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
        + "Wn / Ln (dispersity): %.2f \n" % pdi
        + "standard deviation: %.2f nm \n" % sd
        + "standard deviation / Ln: %.2f nm \n" % sdln
        + r"5% confidence interval: " + "%.2f nm \n" % ci5
        + r"95% confidence interval: " + "%.2f nm \n" % ci95
        )
f.close()

#plot the data as a histogram too
plt.rc ('font', size=8)
plt.figure(1, figsize=(1.75,2.5), dpi= 300)

histogram = plt.hist(all_data,
          bins="auto",
          color="r",
          edgecolor="k",
          label=dir_name
          )
plt.xlabel("Length (nm)")
plt.ylabel("Count")
plt.tight_layout()
plt.legend()
#plt.savefig("histogram.png")

plt.figure(2, figsize=(3.5,2.5), dpi= 300)
sns.displot(all_data, 
              color="r",
              edgecolor="k",
              label=dir_name,
              kde=True
              )

plt.xlabel("Length (nm)")
plt.ylabel("Count")
plt.tight_layout()
plt.legend()
#plt.savefig("histogram.png")


plt.show()