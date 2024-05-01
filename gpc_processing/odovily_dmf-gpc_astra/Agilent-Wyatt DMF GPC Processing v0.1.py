import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.cElementTree as et

#import GPC data from agilent DMF GPC file
def gpc_trace_import_DMF(filename):
    data = np.loadtxt(fname=(f'{filename}'), dtype=str, delimiter=',', unpack='True')
    mw= data[2]
    WFdlogMw = data[3]
    return(mw, WFdlogMw)

#retrieve a list of .csv files from a directory
def get_filenames(directory_in_str, filetype):    
    directory = os.fsencode(directory_in_str)
    filelist = []        
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(filetype): 
            # print(os.path.join(directory, filename))
            filelist.append(filename)
            continue
        else:
            continue       
    return(filelist)

#Retrieve a list of .xml files from a directory

#get GPC data from a list of filenames and the import GPC data function
def get_GPC_Data_from_filelist(filelist):
    mw, WFdlogMw = [],[]
    GPC_Data = []    
    for file in filelist:
        mw, WFdlogMw = gpc_trace_import_DMF(file)
        GPC_Data.append(mw)
        GPC_Data.append(WFdlogMw)
        continue
    master_GPC_data = pd.DataFrame(GPC_Data)
    return(master_GPC_data)

#Extract Key Data from .xml file
def extract_data_from_DMF_GPC_filelist(filelist_xml):
    print('------------------------')
    GPC_Results_Headings = []
    GPC_Results_Data = []    
    for file in filelist_xml:
        xml_tree = et.parse(f'{file}')
        xml_root = xml_tree.getroot()
        print(file)
        #to get a list of children from the xml file:
        #for child in xml_root:
        #    print(child.tag, child.attrib)
        GPC_Results_Headings.append(xml_root[7][4][0].text)
        GPC_Results_Data.append(xml_root[7][4][1].text)
        GPC_Results_Headings.append('Light Scattering')
        GPC_Results_Data.append('Light Scattering')
        GPC_Results_Headings.append(xml_root[7][9][0].text)
        GPC_Results_Data.append(xml_root[7][9][1].text)
        GPC_Results_Headings.append(xml_root[7][17][0].text)
        GPC_Results_Data.append(xml_root[7][17][1].text)
        GPC_Results_Headings.append(xml_root[7][18][0].text)
        GPC_Results_Data.append(xml_root[7][18][1].text)
        GPC_Results_Headings.append('RI')
        GPC_Results_Data.append('RI')
        GPC_Results_Headings.append(xml_root[7][23][0].text)
        GPC_Results_Data.append(xml_root[7][23][1].text)
        GPC_Results_Headings.append(xml_root[7][31][0].text)
        GPC_Results_Data.append(xml_root[7][31][1].text)
        GPC_Results_Headings.append(xml_root[7][32][0].text)
        GPC_Results_Data.append(xml_root[7][32][1].text)
        GPC_Results_Headings.append(xml_root[7][35][0].text)
        GPC_Results_Data.append(xml_root[7][35][1].text)
        GPC_Results_Headings.append(xml_root[7][36][0].text)
        GPC_Results_Data.append(xml_root[7][36][1].text)
        GPC_Results_Headings.append(xml_root[7][37][0].text)
        GPC_Results_Data.append(xml_root[7][37][1].text)
        GPC_Results_Headings.append(xml_root[7][38][0].text)
        GPC_Results_Data.append(xml_root[7][38][1].text)
        GPC_Results_Headings.append(xml_root[7][39][0].text)
        GPC_Results_Data.append(xml_root[7][39][1].text)
        GPC_Results_Headings.append(xml_root[7][41][0].text)
        GPC_Results_Data.append(xml_root[7][41][1].text)
        GPC_Results_Headings.append(xml_root[7][42][0].text)
        GPC_Results_Data.append(xml_root[7][42][1].text)
        GPC_Results_Headings.append(xml_root[7][43][0].text)
        GPC_Results_Data.append(xml_root[7][43][1].text)
        GPC_Results_Headings.append(xml_root[7][44][0].text)
        GPC_Results_Data.append(xml_root[7][44][1].text)
        GPC_Results_Master = pd.DataFrame([GPC_Results_Headings,GPC_Results_Data])
        GPC_Results_Master_T = GPC_Results_Master.T
        print(GPC_Results_Master_T)
        GPC_Results_Master_T.to_csv('Results' + '/' + f'{file}_GPC_Results.csv', index=False, na_rep='')
        np.savetxt('Results' + '/' + f'{file}_GPC_Results.txt', GPC_Results_Master_T.values, fmt='%s')        
    return(GPC_Results_Master_T)


#create a results folder
path = os.path.join(os.getcwd(), 'Results')
os.makedirs(path)

#get a list of the filenames
directory_in_str = os.getcwd()
#get a list of .csv files in the current directory
filelist_csv = get_filenames(directory_in_str, '.csv')
print(filelist_csv)
#extract GPC data from the .csv files in the current folder
GPC_data_Table = get_GPC_Data_from_filelist(filelist_csv)
#output these files to an arrayed .csv file for future graphing
GPC_data_Table_T = GPC_data_Table.T
print('------------------------')
print(GPC_data_Table_T)
GPC_data_Table_T.to_csv('Results' + '/' + 'arrayed_GPC_traces.csv', index=False, na_rep='')

#get list of xml files in current directory:
filelist_xml = get_filenames(directory_in_str, '.xml')
#extract key data from xml file:
GPC_Results = extract_data_from_DMF_GPC_filelist (filelist_xml)



#TO DO
#sort GPC traces by name
#add GPC trace name to excel sheet








    



#TESTING
#Test GPC Data Import
#test = input('What is your GPC filename? ')
#mw, WFdlogMw = gpc_trace_import_DMF(test)
#print(mw)
#print('_________________')
#print(WFdlogMw)

#print(GPC_Results_Headings)
#print(GPC_Results_Data)