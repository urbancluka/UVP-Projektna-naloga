#The purpose of this file is to contain a funcion which recieves a website and extracts the data on all the cars, which are shown on the site. 
import re

def get_urls_from_main(file):
    """Function returns a list of all link to car pages for further scrapping. File HAS to be from the main page of the website"""
    with open(f"websites/{file}", "r") as f:
        text = f.read()
        re_link = r'<div class="col-4"> <a href="(.*?)" title="'
        urls = re.findall(re_link, text)
        return urls

def get_content_from_car_page(file):
    """File extracts data for given car"""
    

