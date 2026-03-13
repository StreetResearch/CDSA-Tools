This script was written for a Shimadzu HPLC equipped with a PDA detector.

ensure you have installed python and the following packages first:
numpy
pandas
matplotlib
seaborn
scipy
hplc-py
colorama

to run the script, set the method to export data from each run as a csv,
and set it to export the sample information and PDA data. 
The PDA data should appear at the same line of the csv file as in the example. 

place the .py script, .ps1 and .bat files into the folder with a collection of PDA-data.csv files
run the .bat file to execute the script and process all HPLC traces

This script is provided under a GPL-3 licence as open source software
please credit the following github page if reused:
https://github.com/StreetResearch/CDSA-Tools

tested as working on python v3.10