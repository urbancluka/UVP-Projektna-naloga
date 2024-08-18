"""
File contains all functions related to saving of data to ordered .csv files as well as creating .csv files to save to. 
"""
import csv
import pandas as pd  

def create_main_csv(csv_name, list_of_fields=["Id",
                                              "Price (EUR)",
                                              "Transmission", 
                                              "Number of Gears",
                                              "Body Type",
                                              "Number of seats",
                                              "Drive wheel",
                                              "Fuel Type",
                                              "Number of Cylinders",
                                              "Volume of engine",
                                              "Power",
                                              "Max Torque",
                                              "Top Speed",
                                              "Acceleration to 100km/h",
                                              "Combined consumption l/100km"]):
    """Function creates a .csv file with the fields given in the list list_of_fields. Returns None"""
    with open(f"{csv_name}", "w") as f:
        write = csv.writer(f)
        write.writerow(list_of_fields)

def save_list_to_csv(list_of_data, file_name="data.csv"):
    """Function writes list of data into an existing .csv file."""
    with open(f"{file_name}", "a+") as f:
        write = csv.writer(f)
        write.writerow(list_of_data)