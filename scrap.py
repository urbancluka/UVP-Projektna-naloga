#The purpose of this file is to contain a funcion which recieves a website and extracts the data on all the cars, which are shown on the site. 
import re

def get_urls_from_main(file):
    """Function returns a list of all link to car pages for further scrapping. File HAS to be from the main page of the website"""
    with open(f"websites/{file}", "r") as f:
        content = f.read()
        re_link = r'<div class="col-4"> <a href="(.*?)" title="'
        urls = re.findall(re_link, content)
        return urls
    
def extract_name_and_id(list_of_urls):
    """Function takes a list of urls and returns a dict of the form {id: [name, url]}. Used then to save car pages"""
    dict_id = {}
    for url in list_of_urls:
        re_id = r'-specs/(\d*)'
        id = int(re.search(re_id, url).group()[7:])
        re_name = r'https://www.cars-data.com/en/(.*?)-specs'
        name = re.search(re_name, url).group()[29:-6]
        dict_id[id] = [name, url]
    print(dict_id)
    return dict_id

def get_content_from_car_page(file):
    """File extracts data for given car. Returns a dict. Data: price, transmission, body type, number of seats, drive wheel, fuel type, engine capacity, power(kW/hp), max torque, top speed, acceleration, consumption"""
    with open(f"cars/{file}", "r") as f:
        content = f.read()
        re_name = r'<span itemprop="name">(.?*)</span>'
        print(re.findall(re_name, content))

print(extract_name_and_id(get_urls_from_main("page1"))[1])
