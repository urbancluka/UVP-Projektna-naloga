#This file contains the function to download the .html file from the internet and saves it to local memory. 
import requests


#Set website url:
#url = f"https://www.cars-data.com/en/all-cars/page{page_number}.html"

#Set file_name:
#file_name = f"page{page_number}"

#Starting page number:
starting_page_number = 1
#Max page number:
max_page_number = 5

#https://www.cars-data.com/en/all-cars/page1.html -- https://www.cars-data.com/en/all-cars/page97.html

def download_main(i, file_name):
    url = f"https://www.cars-data.com/en/all-cars/page{i}.html"
    """
    Function takes the page number of desired site and the names of the file, to be saved as. Function returns None.
    """
    response = requests.get(url)
    print(f"URL of downloaded website: {response.url}")
    if response.ok:
        print("Response OK. Downloading site...")
        with open(f"websites/{file_name}", "wb") as file:
            file.write(response.content)
            print("Website saved to memory")
    else:
        print(f"Error! error code: {response.status_code}")
    return

#for index in range(starting_page_number, max_page_number + 1):
#   download_main(index, f"page{index}")


#https://www.cars-data.com/en/abarth-500-1-4-16v-t-jet-specs/1
#This wont work. Need to find a way to save car sites. 
def download_cars(dict_id):
    """Function takes a dict of type [[id, name, url]] and saves the site under the id"""

    response = requests.get(url)
    #url = https://www.cars-data.com/en/abarth-500-1-4-16v-t-jet-specs/123455
    file_name = 0
    print(file_name)
    print(f"URL of downloaded website: {response.url}")
    if response.ok:
        print("Response OK. Downloading site...")
        with open(f"cars/{file_name}", "wb") as file:
            file.write(response.content)
            print("Website saved to memory")
    else:
        print(f"Error! error code: {response.status_code}")
    return

download_cars("https://www.cars-data.com/en/abarth-500-1-4-16v-t-jet-specs/1")

