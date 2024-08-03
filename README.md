# UVP-Projektna-naloga
Naloga je pridobiti podatke s HTML strani *https://www.cars-data.com/en/all-cars.html* in napraviti analizo teh podatkov s pomočjo Pandas

## TODO:
 - [ ] Create function to download .html file with correct parameters
 - [ ] Decide what website to scrap
 - [ ] Write regex function to retrieve data from raw html file
 - [ ] Save data to single .csv file
 - [ ] Make website inputs a prompt for the user to enter ("enter starting page, enter last page...")
 - [ ] Add content type for download function -> merge download_main and download_cars by adding another parameter type: main/car
 - [ ] Build loop into download_main function
 - [ ] Fix power scrapping
 - [ ] Add test to see if file is empty in save_csv.py -> save_list_to_csv
 - [ ] Add test to see if list_of_data is same length as csv head