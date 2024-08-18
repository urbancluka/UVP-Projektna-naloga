"""
This file contains the functions to download the .html files from the internet and saves it to local memory. 
download_main() for main page downloads, saved to "websites" folder
download_cars() saves the specific cars website to the folder "cars" folder
"""

import requests

def download_main(i: int):
    url = f"https://www.cars-data.com/en/all-cars/page{i}.html"
    """
    Function takes the page number of desired site and saves it to websites/. Function returns None.
    """
    response = requests.get(url) #Get file from url
    print(f"URL of downloaded website: {response.url}") # Get URL of website
    if response.ok: #Test response code
        print("Response OK. Downloading site...")
        with open(f"websites/page{i}.html", "wb") as file:
            file.write(response.content) # Save file to memory
            print("Website saved to memory")
    else:
        print(f"Error! error code: {response.status_code}")
        return
    

def download_cars(list_id: list):
    """Function takes a list of type [[id, name, url]] and saves the site under the id"""
    for item in list_id:
        response = requests.get(item[2]) # Get website
        print(f"URL of downloaded website: {response.url}") # Print URL 
        if response.ok: # Check response
            print("Response OK. Downloading site...")
            with open(f"cars/{item[0]}.html", "wb") as file:
                file.write(response.content)  # Save to memory
                print("Website saved to memory")
        else:
            print(f"Error! error code: {response.status_code} at url {item[2]}") # Raise error and print file for easier debugging
        
    return


# TEST CASE
# download_cars([[2, 'abarth-500c-1-4-16v-t-jet', 'https://www.cars-data.com/en/abarth-500c-1-4-16v-t-jet-specs/2']])



