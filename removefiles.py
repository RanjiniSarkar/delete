import os
import shutil
import time

deletedFileCount = 0
deletedFolderCount = 0
path = "/pathToDelete"
days = 30
seconds = time.time()-(days*24*60*60)
if os.path.exist(path):
    for root_folder,folders,files in os.walk(path):
        if seconds >= getFileOrFolderAge(root_folder):
            remove_folder(root_folder)
            deletedFolderCount+=1
            break
        else: 
            for folder in folders: 
                folder_path = os.pah.join(root_folder, folder)
                

                if seconds >= getFileOrFolderAge(folder_path):
                    remove_folder(folder_path)
                    deletedFolderCount+=1
            
            for file in files:
                file_path = os.path.join(folder_path,file_path)

                if seconds >= getFileOrFolderAge(file_path):
                    remove_file(file_path)
                    deletedFileCount+=1
        
else:
    seconds >= getFileOrFolderAge(path)
    remove_file(path)
    deletedFileCount+=1

else:
    print("path is not found")
    deletedFileCount+=1

def remove_folder(path):
    if not shutil.rmtree(path):
        print("path is removed successfully")
    else:
        print("unable to delete the path")

def remove_file(path):
    if not os.remove(path):
         print("path is removed successfully")
    else:
        print("unable to delete the path")

def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime 

main()



