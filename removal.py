#This file will contain the functions to remove files from the directories

import os

def delet_contents_of_folder(path_to_folder):
    files = os.listdir(path_to_folder)
    for file in files:
        file_path = os.path.join(path_to_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

def delete_csv():
    files = os.listdir(".")
    for file in files:
        if file.endswith(".csv"):
            os.remove(file)



