import os
import shutil
import time

path = 'C:/Users/User/Desktop/files/js'
day = 30
second = time.time() - (day * 60 * 60 * 24) 
def main():
    if(os.path.exists(path)):
        for  main_folder,folder,files in os.walk(path):
            if(second >= get_age(main_folder)):
                remove_folder(main_folder)
                break
            else:
                for subfolder in folder:
                    path_of_folder = os.path.join(main_folder, subfolder)

                    if(path_of_folder >= get_age(path_of_folder)):
                        remove_folder(path_of_folder)
                for file in files:
                    filePath = os.path.join(main_folder, file)

                    if(second >= get_age(filePath)):
                        remove_file(filePath)
        else:
            if(second >= get_age(path)):
                remove_folder(path)
    else:
        print("Path Not Found")



def remove_file(path):
	if not os.remove(path):
		print(f"{path} is removed successfully")
	else:
		print("Unable to delete the "+path)

def remove_folder(path):
	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")

	else:
		print(f"Unable to delete the "+path)

def get_age(path):
    return os.stat(path).st_ctime

main()