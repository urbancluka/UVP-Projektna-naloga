#This file contains the actual program that scraps the website. All that is needed to run the scrapping is to run this file.

#Importing auxiliary files
import download_file as dnf
import save_csv as scsv
import scrap as sc
import removal as rem
import os

############################## CLEARING FILES AND FOLDERS ##############################
rem.delet_contents_of_folder("websites/")
rem.delet_contents_of_folder("cars/")


############################## INPUT OF STARTING AND ENDING PAGE ##############################
valid_start_stop_conditions = False
print("Pozdravljeni v programu za pridobivanje podatkov s spletne strani cars-data.com. \n")
input("Za nadaljevanje pritisnite tipko 'Enter' na vasi tipkovnici...")
while not valid_start_stop_conditions:
    starting_page = input("Prosimo, vnesite zacetno stran (stevilko), na kateri bi zaceli s zajemom podatkov. Stevilo mora biti manj od 97:\n")
    if starting_page.isnumeric():
        if int(starting_page) in range(1, 98):
            starting_page = int(starting_page)
            ending_page = input("Prosimo, vnesite se koncno stran:\n")
            if ending_page.isnumeric:
                ending_page = int(ending_page)
                if ending_page > starting_page:
                    print(f"Tvoj zajem se bo zacel na strani {starting_page} in koncal na strani {ending_page}. Ce si se zmotil, pozeni program se enkrat.")
                    valid_start_stop_conditions = True
                else:
                    print("Prepricajte se, da je zacetna manjsa od koncne. Poskusite znova")
            else:
                print("Prosim vnesite stevilo.")
        else:
            print("Stevilka ni veljavna. Ustrezati mora 1 <= stevilka < 97")
    else:
        print("To ni veljaven znak")

for i in range(starting_page, ending_page + 1):
    dnf.download_main(i)

############################## DOWNLOAD INITIAL DATA ##############################
print("Zajem podatkov se zacenja:")
for i in range(starting_page, ending_page + 1):
    dnf.download_main(i)
print("Zajem podatkov koncan!")



    
