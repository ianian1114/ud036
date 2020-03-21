import os
import re
def rename_files():
    #(1) get files names from a folder
    file_list = os.listdir(r"/Users/Jones_MAC/Desktop/prank")
    #print(files_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"/Users/Jones_MAC/Desktop/prank")
    #(2) for each file,rename filename
    for file_name in file_list:
        #os.rename(file_name,file_name.translate((None,"0123456789")))
        os.rename(file_name,re.sub("[0-9]","", file_name))
        os.chdir(saved_path)
rename_files()
