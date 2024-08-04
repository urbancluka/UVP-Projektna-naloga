#This file contains the functions related to saving data stored in python objects into organised .csv files.
import csv
#              id  price   transmission                     body type           seats drive    fuel type  cylinders power   torque topspeed  acceleration    consumption
#list_of_data = [2, 25500, '5 speed manual transmission', '3-doors, convertible', 4, 'front', 'gasoline', 4, 1368, 'power', 206,      205,   7.9,            6.5]

def create_main_csv(csv_name, list_of_fields=["Id",
                                              "Price (EUR)",
                                              "Transmission", 
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
    with open(f"{file_name}", "a") as f:
        #add a check if file is empty: if so, stop the function.
        #add check to see if lenth of list_of_data is the same as csv head
        write = csv.writer(f)
        write.writerow(list_of_data)

    

