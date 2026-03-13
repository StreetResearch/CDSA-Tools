This script was written for a Shimadzu HPLC equipped with a PDA detector

To use, install python and the following packages:
numpy
pandas
matplotlib
seaborn
scipy
hplc-py
colorama

The HPLC method should be set to automatically generate a .csv data file after the sample has run
this file should contain the sample information and the PDA data only

For the script to work correctly, the PDA data should begin on the same line as in the example csv data.

To run, place the .py script, .ps1, and .bat files into a folder with the set of csv files to be processed.
execute the .bat file to begin the processing.

This script is provided under a GPL-3.0 licence as open source software. If you reuse it, please credit:
https://github.com/StreetResearch/CDSA-Tools/

Tested as working on python 3.10