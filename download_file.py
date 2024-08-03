#This file contains the function to download the .html file from the internet and saves it to local memory.
import requests

#Set website url
url = "https://eventregistry.org/intelligence?tab=items&searchMode=concept&type=articles&conditions=3-en-Poverty-Poverty&dateStart=2024-07-03&dateEnd=2024-08-03&percentileRange=0&percentileRange=100&forceMaxDataTimeWindow=31&dataType=news"
#Second page:
# "https://eventregistry.org/intelligence?tab=items&searchMode=concept&type=articles&conditions=3-en-Poverty-Poverty&dateStart=2024-07-03&dateEnd=2024-08-03&percentileRange=0&percentileRange=100&forceMaxDataTimeWindow=31&dataType=news"

download_params = {"downloadformat": "html"}

def download(url, file_name):
    """
    Function takes the url of desired site and the names of the file, to be saved as. Function returns None.
    """
    response = requests.get(url)
    print(f"URL of downloaded website: {response.url}")
    if response.ok:
        with open(file_name, "wb") as file:
            file.write(response.content)
    else:
        print(f"Error! erroe code: {response.status_code}")
        return