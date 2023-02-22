---
GPC processing for Malvern Omnisec v10+ software
---

Instructions:

1) place the plotgpcdata_fishy.py file into a folder
2) in omnisec v10 process your trace as normal.
3) on the 'manner report' report of the omnisec software, find the plot of WFdLogMw vs Mw and copy the data to excel and save as a .csv
3) add all of the .csv files to the folder with the python file. Ensure they have simple names (ie the codename of the sample)
4) open the python file with a text editor e.g. notepad++ and customize the graph options, which are on lines 63-77 (e.g. change the legend labels)
5) run the python file, follow the instructions
6) you should get an arrayed table of data and a plot of the datasets overlaid...
6) voila! enjoy your gpc data =)