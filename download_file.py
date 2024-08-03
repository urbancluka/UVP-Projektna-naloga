#This file contains the function to download the .html file from the internet and saves it to local memory.
import requests


#Set website url
url = ""
#Set file_name:
file_name = ""
#Number of pages:
pages = 0
#https://www.cars-data.com/en/all-cars/page1.html -- https://www.cars-data.com/en/all-cars/page97.html

def download(url, file_name):
    """
    Function takes the url of desired site and the names of the file, to be saved as. Function returns None.
    """
    response = requests.get(url)
    print(f"URL of downloaded website: {response.url}")
    if response.ok:
        with open(f"websites/{file_name}", "wb") as file:
            file.write(response.content)
    else:
        print(f"Error! erroe code: {response.status_code}")
        return

download(url, file_name)