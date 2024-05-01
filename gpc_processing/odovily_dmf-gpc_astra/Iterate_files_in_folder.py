import os

#make a function to get a list of files from a directory
def get_filenames(directory_in_str):
    
    directory = os.fsencode(directory_in_str)
    filelist = []        
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"): 
            # print(os.path.join(directory, filename))
            filelist.append(filename)
            continue
        else:
            continue       
    return(filelist)

#get a list of the filenames
directory_in_str = os.getcwd()
#directory_in_str = input('what is the directory you want to examine ')
filelist = get_filenames(directory_in_str)
print(filelist)