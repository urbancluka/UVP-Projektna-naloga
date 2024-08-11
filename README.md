# UVP-Projektna-naloga
Naloga je pridobiti podatke s HTML strani *https://www.cars-data.com/en/all-cars.html* in napraviti analizo teh podatkov s pomočjo Pandas



## TODO:
 - [x] Create function to download .html file with correct parameters
 - [x] Decide what website to scrap
 - [x] Write regex function to retrieve data from raw html file
 - [x] Save data to single .csv file
 - [x] Make website inputs a prompt for the user to enter ("enter starting page, enter last page...")
 - [x] Build loop into download_main function
 - [x] Fix power scrapping
 - [ ] Add test to see if file is empty in save_csv.py -> save_list_to_csv
 - [ ] Add test to see if list_of_data is same length as csv head
 - [x] Fix missing data point in acceleration