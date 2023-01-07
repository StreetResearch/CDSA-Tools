#----set up modules----
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

#----setup global variables----:
dir_name = os.path.relpath(".","..")

#----define the functions used to plot the data----:

#function used to load the csv file with the length results in (only loads and returns 'length' column)
def loaddata(filename):
        #find the length column
        header = np.loadtxt (fname=f"{filename}.csv", dtype=str, delimiter=",", max_rows=1, unpack = False)
        header = header.tolist()
        length_col_index = header.index("Length")

        #load data
        loaded_data = np.loadtxt(fname=(f"{filename}.csv"), dtype=float, delimiter=",", skiprows=1, usecols = (length_col_index), unpack = True)
        return loaded_data

#create the 'getstats' function - will output a text file with the stats of the micelle lengths
def getstats(dataset):

        #find statistics of the length data
        #easy stats first
        number_counted = len(dataset)
        ln = np.mean(dataset)
        ci5 = np.percentile(dataset, 5)
        ci95 = np.percentile(dataset, 95)
        sd = np.std(dataset)
        sdln = sd/ln
        #calculate weight average length
        length2 = dataset**2
        Elength2 = sum(length2)
        Elength = sum(dataset)
        wn = Elength2/Elength
        #calculate the dispersity
        pdi = wn/ln

        #output data to a text file
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

def getnormhistogram(datatoplot):
        #plot the data as a histogram too
        plt.rc ('font', size=8)
        plt.figure(1, figsize=(2.5,2.5), dpi= 600)

        histogram = plt.hist(datatoplot,
                bins="auto",
                density=True,
                stacked=True,
                color="r",
                edgecolor="k",
        #          label=dir_name
                )
        plt.xticks(np.arange(0, round(max(datatoplot)), round(max(datatoplot/5))))
        plt.yticks(np.arange(0, 0.08, 0.01))
        plt.xlabel("Length (nm)")
        plt.ylabel("Normalized Count")
        plt.tight_layout()
        #plt.legend()
        plt.savefig("normalized_histogram.png")

def gethistogram(datatoplot):
        sns.displot(datatoplot, 
                color="r",
                edgecolor="k",
                label=dir_name,
                kde=True,
                height=2.5,
                aspect=3.5/2.5
                )

        plt.xlabel("Length (nm)")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.legend()
        plt.savefig("histogram_with_density.png", dpi=600)

#plt.show()

#----run functions on the dataset----
all_data = loaddata("Results")
getstats(all_data)
getnormhistogram(all_data)
gethistogram(all_data)