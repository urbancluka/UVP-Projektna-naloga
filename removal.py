"""
File contains functions related to the removal of files and clearing of folders
"""

import os

def delet_contents_of_folder(path_to_folder):
    """Functions clears contents of given folder"""
    files = os.listdir(path_to_folder)
    for file in files:
        file_path = os.path.join(path_to_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


def delete_csv():
    """Functions removes all .csv files in working directory. Used to clear 'data.csv' and 'auxillary.csv' """
    files = os.listdir(".")
    for file in files:
        if file.endswith(".csv"):
            os.remove(file)



