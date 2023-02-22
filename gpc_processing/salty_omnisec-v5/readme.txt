---
GPC processing for Malvern Omnisec v5 software
---

Instructions:

1) place the plotgpcdata_salty.py file into a folder
2) in omnisec v5 process your trace as normal.
3) when done, go 'file > export' to export your processed data as a .txt file
3) add all of the .txt files to the folder with the python file. Ensure they have simple names (ie the codename of the sample)
4) open the python file with a text editor e.g. notepad++ and customize the graph options, which are on lines 74-88 (e.g. change the legend labels)
5) run the python file, follow the instructions
6) you should get a properly formatted data table for each sample, an arrayed table of data to plot, and a plot of the datasets overlaid...
6) voila! enjoy your gpc data =)