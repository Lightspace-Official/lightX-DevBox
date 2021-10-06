
# importing required modules
from zipfile import ZipFile
from tkinter import filedialog
from tkinter import *
import os
  
def get_all_file_paths(directory):
  
    # initializing empty file paths list
    file_paths = []
  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # returning all file paths
    return file_paths

root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
  
def main():
    # path to folder which needs to be zipped
    directory = folder_selected
  
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)
  
    # printing the list of all files to be zipped
    print('Following files will be lX Packaged:')
    for file_name in file_paths:
        print(file_name)
  
    # writing files to a zipfile
    with ZipFile('Untitled.lxpkg','w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
  
    print('All files Packaged successfully')        
  
  
if __name__ == "__main__":
    main()
