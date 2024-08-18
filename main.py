"""
This file contains the actual program that scraps the website. All that is needed to run the scrapping is to run this file and 
give required user inputs. Functions called in this file are defined in other .py files in directory.
"""

#Importing auxiliary files
import download_file as dnf
import save_csv as scsv
import scrap as sc
import removal as rem
import os


def main():
    ############################## CLEARING FILES AND FOLDERS ##############################
    #Delete files if folders exist
    try:
        rem.delet_contents_of_folder("websites/")
        rem.delet_contents_of_folder("cars/")
        rem.delete_csv()
    except:
        pass

    #Add websites and cars folder if they dont exist
    newpath = ["./websites" , "./cars"]
    for path in newpath:
        if not os.path.exists(path):
            os.makedirs(path)


    ############################## INPUT OF STARTING AND ENDING PAGE ##############################
    valid_start_stop_conditions = False
    print("Pozdravljeni v programu za pridobivanje podatkov s spletne strani cars-data.com. \n")
    print("Program vas bo prosil za vnos stevilk. To storite tako, da vnesete stevilko, nato pa pritisnite 'Enter' na vasi tipkovnici.")
    while not valid_start_stop_conditions:
        starting_page = input("Prosimo, vnesite zacetno stran (stevilko), na kateri bi zaceli s zajemom podatkov. Stevilo mora biti manj od 97. Predlagamo, da zacnete z 1:\n")
        if starting_page.isnumeric():
            if int(starting_page) in range(1, 98):
                starting_page = int(starting_page)
                ending_page = input("Prosimo, vnesite se koncno stran. Predlagamo, da koncate pri 97:\n")
                if ending_page.isnumeric:
                    ending_page = int(ending_page)
                    if ending_page >= starting_page:
                        print(f"Tvoj zajem se bo zacel na strani {starting_page} in koncal na strani {ending_page}. Ce si se zmotil, pozeni program se enkrat.")
                        valid_start_stop_conditions = True
                    else:
                        print("Prepricajte se, da je zacetna manjsa od koncne. Poskusite znova")
                else:
                    print("Prosim vnesite stevilo.")
            else:
                print("Stevilka ni veljavna. Ustrezati mora 1 <= stevilka <= 97")
        else:
            print("To ni veljaven znak")

    ############################## DOWNLOAD INITIAL DATA ##############################
    print("Zajem podatkov se zacenja:")
    for i in range(starting_page, ending_page + 1):
        dnf.download_main(i)
    print("Zajem podatkov koncan!")

    ############################## RETRIEVE DATA FOR EVERY FILE IN WEBSITES/ ##############################
    list_of_files = os.listdir("websites/")

    scsv.create_main_csv("auxillary.csv", list_of_fields=["Id", "Name", "Url"])
    scsv.create_main_csv("data.csv")
    for file in list_of_files:
        urls = sc.get_urls_from_main(file)
        id_name_url = sc.extract_name_and_id(urls)
        dnf.download_cars(id_name_url)
        for temp_list in id_name_url:
            scsv.save_list_to_csv(temp_list, file_name="auxillary.csv")
            data = sc.get_content_from_car_page(temp_list[0])
            scsv.save_list_to_csv(data)
    print("Vase datoteke se nahajajo v datoteki 'data.csv'")

main()



    
