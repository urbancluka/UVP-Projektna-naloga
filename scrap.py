#The purpose of this file is to contain a funcion which recieves a website and extracts the data on all the cars, which are shown on the site. 
import re

def get_urls_from_main(file):
    """Function returns a list of all link to car pages for further scrapping. File HAS to be from the main page of the website"""
    with open(f"websites/{file}", "r") as f:
        content = f.read()
        re_link = r'<div class="col-4"> <a href="(.*?)" title="'
        urls = re.findall(re_link, content)
        for index in range(len(urls)):
            urls[index] = urls[index] + "/tech"
        return urls

def extract_name_and_id(list_of_urls):
    """Function takes a list of urls and returns a list of the form [ [id, name, url] ]. Used then to save car pages"""
    list_id = []
    for url in list_of_urls:
        re_id = r'-specs/(\d*)'
        id = int(re.search(re_id, url).group()[7:])
        re_name = r'https://www.cars-data.com/en/(.*?)-specs'
        name = re.search(re_name, url).group()[29:-6]
        list_id.append([id, name, url])
    return list_id

#print(extract_name_and_id(get_urls_from_main("page1.html")))

def get_content_from_car_page(id):
    """
    File extracts data for given car. Returns a list of data. 
    Data: 
    - ID,
    - price, 
    - transmission, 
    - number of gears,
    - body type, 
    - number of seats, 
    - drive wheel, 
    - fuel type, 
    - number of cylinders
    - engine capacity, 
    - power(kW/hp), 
    - max torque, 
    - top speed, 
    - acceleration, 
    - consumption"""
    list_of_data = [id]
    with open(f"cars/{id}.html", "r") as f:
        content = f.read()

        re_price = r'Price:</td><td class="col-6 grey">&euro; (.*?)</td></tr>'
        try:
            price = re.findall(re_price, content)[0]
            price = re.sub("[.]", "", price)
            price = int(price)
        except (ValueError, IndexError) as e:
            price = "NaN"
        list_of_data.append(price)
        

        re_transmission = r'Transmission:</td><td class="col-6 grey">(.*?)</td>'
        try:
            transmission = re.findall(re_transmission, content)[0]
        except (ValueError, IndexError) as e:
            transmission = "NaN"
        list_of_data.append(transmission)

        re_number_of_gears = r'Transmission:</td><td class="col-6 grey">(.*?)</td>'
        try:
            number_of_gears = re.findall(re_number_of_gears, content)[0]
            number_of_gears = number_of_gears[0]
            number_of_gears = int(number_of_gears)
        except (ValueError, IndexError) as e:
            number_of_cylinders = "NaN"
        list_of_data.append(number_of_gears)

        re_body_type = r'Body Type:</td><td class="col-6">(.*?)</td>'
        try:
            body_type = re.findall(re_body_type, content)[0]
        except (ValueError, IndexError) as e:
            body_type = "NaN"
        list_of_data.append(body_type)

        re_number_of_seats = r'Number Of Seats:</td><td class="col-6">(.*?)</td>'
        try:
            number_of_seats = re.findall(re_number_of_seats, content)[0]
            number_of_seats = int(number_of_seats)
        except (ValueError, IndexError) as e:
            number_of_seats = "NaN"
        list_of_data.append(number_of_seats)

        re_drive_wheel = r'Drive Wheel :</td><td class="col-6 grey">(.*?)</td>'
        try:
            drive_wheel = re.findall(re_drive_wheel, content)[0]
        except (ValueError, IndexError) as e:
            drive_wheel = "NaN"
        list_of_data.append(drive_wheel)

        re_fuel_type = r'Fuel Type:</td><td class="col-6 grey">(.*?)</td>'
        try:
            fuel_type = re.findall(re_fuel_type, content)[0]
        except (ValueError, IndexError) as e:
            fuel_type = "NaN"
        list_of_data.append(fuel_type)

        re_number_of_cylinders = r'Cylinders:</td><td class="col-6 grey">(.*?)</td>'
        try:
            number_of_cylinders = re.findall(re_number_of_cylinders, content)[0]
            number_of_cylinders = re.sub("[^0-9]", "", number_of_cylinders)
            number_of_cylinders = int(number_of_cylinders)
        except (ValueError, IndexError) as e:
            number_of_cylinders = "NaN"
        list_of_data.append(number_of_cylinders)

        re_engine_capacity = r'Engine Capacity:</td><td class="col-6 grey">(.*?) cc</td>'
        try:
            engine_capacity = re.findall(re_engine_capacity, content)[0]
            engine_capacity = int(engine_capacity)
        except (ValueError, IndexError) as e:
            engine_capacity = "NaN"
        list_of_data.append(engine_capacity)

        re_power = r'Total Max. Power \(hp\):</td><td class="col-6">(.*?)</td></tr><tr class="'
        try:
            power = re.findall(re_power, content)[0]
            power = int(power)
        except (ValueError, IndexError) as e:
            power = "NaN"
        list_of_data.append(power)

        re_torque = r'Max Torque:</td><td class="col-6 grey">(.*?) nm</td>'
        try:
            torque = re.findall(re_torque, content)[0]
            torque = int(torque)
        except (ValueError, IndexError) as e:
            torque = "NaN"
        list_of_data.append(torque)

        re_top_speed = r'Top Speed:</td><td class="col-6 grey">(.*?) km/h</td>'
        try:
            top_speed = re.findall(re_top_speed, content)[0]
            top_speed = float(top_speed)
        except (ValueError, IndexError) as e:
            top_speed = "NaN"
        list_of_data.append(top_speed)

        re_acceleration = r'Acceleration 0-100 Km / H:</td><td class="col-6">(.*?) s</td>'
        try:
            acceleration = re.findall(re_acceleration, content)[0]
            acceleration = re.sub(",", r".", acceleration)
            acceleration = float(acceleration)
        except (ValueError, IndexError) as e:
            acceleration = "NaN"
        list_of_data.append(acceleration)

        re_combined_consumption = r'Combined Consumption:</td><td class="col-6 grey">(.*?) l/100km</td>'
        try:
            combined_consumption = re.findall(re_combined_consumption, content)[0]
            combined_consumption = re.sub(",", r".", combined_consumption)
            combined_consumption = float(combined_consumption)
        except (ValueError, IndexError) as e:
            combined_consumption = "NaN"
        list_of_data.append(combined_consumption)

        return list_of_data
    

#TEST CASE
#print(get_content_from_car_page(2))
