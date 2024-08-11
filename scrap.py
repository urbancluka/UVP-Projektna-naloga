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
        price = re.findall(re_price, content)[0]
        price = re.sub("[.]", "", price)
        try:
            price = int(price)
        except:
            price = "NaN"
        list_of_data.append(price)
        

        re_transmission = r'Transmission:</td><td class="col-6 grey">(.*?)</td>'
        transmission = re.findall(re_transmission, content)[0]
        list_of_data.append(transmission)

        re_body_type = r'Body Type:</td><td class="col-6">(.*?)</td>'
        body_type = re.findall(re_body_type, content)[0]
        list_of_data.append(body_type)

        re_number_of_seats = r'Number Of Seats:</td><td class="col-6">(.*?)</td>'
        number_of_seats = re.findall(re_number_of_seats, content)[0]
        try:
            number_of_seats = int(number_of_seats)
        except:
            number_of_seats = "NaN"
        list_of_data.append(number_of_seats)

        re_drive_wheel = r'Drive Wheel :</td><td class="col-6 grey">(.*?)</td>'
        drive_wheel = re.findall(re_drive_wheel, content)[0]
        list_of_data.append(drive_wheel)

        re_fuel_type = r'Fuel Type:</td><td class="col-6 grey">(.*?)</td>'
        fuel_type = re.findall(re_fuel_type, content)[0]
        list_of_data.append(fuel_type)

        re_number_of_cylinders = r'Cylinders:</td><td class="col-6 grey">(.*?)</td>'
        number_of_cylinders = re.findall(re_number_of_cylinders, content)[0]
        number_of_cylinders = re.sub("[^0-9]", "", number_of_cylinders)
        try:
            number_of_cylinders = int(number_of_cylinders)
        except:
            number_of_cylinders = "NaN"
        list_of_data.append(number_of_cylinders)

        re_engine_capacity = r'Engine Capacity:</td><td class="col-6 grey">(.*?) cc</td>'
        engine_capacity = re.findall(re_engine_capacity, content)[0]
        try:
            engine_capacity = int(engine_capacity)
        except:
            engine_capacity = "NaN"
        list_of_data.append(engine_capacity)

        #Power doesnt work
        re_power = r'Total Max. Power \(hp\):</td><td class="col-6">(.*?)</td></tr><tr class="'
        power = re.findall(re_power, content)[0]
        try:
            power = int(power)
        except:
            power = "NaN"
        list_of_data.append(power)

        re_torque = r'Max Torque:</td><td class="col-6 grey">(.*?) nm</td>'
        torque = re.findall(re_torque, content)[0]
        try:
            torque = int(torque)
        except:
            torque = "NaN"
        list_of_data.append(torque)

        re_top_speed = r'Top Speed:</td><td class="col-6 grey">(.*?) km/h</td>'
        top_speed = re.findall(re_top_speed, content)[0]
        try:
            top_speed = float(top_speed)
        except:
            top_speed = "NaN"
        list_of_data.append(top_speed)

        re_acceleration = r'Acceleration 0-100 Km / H:</td><td class="col-6">(.*?) s</td>'
        acceleration = re.findall(re_acceleration, content)[0]
        acceleration = re.sub(",", r".", acceleration)
        try:
            acceleration = float(acceleration)
        except:
            acceleration = "NaN"
        list_of_data.append(acceleration)

        re_combined_consumption = r'Combined Consumption:</td><td class="col-6 grey">(.*?) l/100km</td>'
        combined_consumption = re.findall(re_combined_consumption, content)[0]
        combined_consumption = re.sub(",", r".", combined_consumption)
        try:
            combined_consumption = float(combined_consumption)
        except:
            combined_consumption = "NaN"
        list_of_data.append(combined_consumption)

        return list_of_data
    

#TEST CASE
#print(get_content_from_car_page(2))
