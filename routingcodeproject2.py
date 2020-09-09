import googlemaps
import requests
import pandas as pd
import urllib.request
import json
import numpy as np
from tkinter import *
api_key = "AIzaSyBhIrlJ_lHYKdwMRna4NAOtUPdpK40DQMo"
gmaps = googlemaps.Client(key=api_key)


def get_dist(x, y):
    return gmaps.distance_matrix(x.replace(" ", "+"), y.replace(" ", "+"))["rows"][0]["elements"][0]["duration"]["text"]


tech_lst = []
tech_dict = {}

class Technician:
    def __init__(self, name, area, abilities, max_num, phone_num, home, cx_list, cx_dist = []):
        self.name = name
        self.area = area
        self.abilities = abilities
        self.max_num = max_num
        self.phone_num = phone_num
        self.home = home
        self.cx_list = cx_list
        self.cx_dist = cx_dist
        tech_dict[self.name] = self.name, self.area, self.abilities, self.max_num, self.phone_num, self.home, \
                               self.cx_list
        tech_lst.append(self)
    def initials(self):
        return list(self.name[0])[0], list(self.name.split()[1])[0]


cx_dict = {}


class Customer:
    def __init__(self, cx_name, address, appliance_type, appliance_brand, appliance_issue, date, time_frame, email,
                 phone, dist=[]):
        self.cx_name = cx_name
        self.address = address
        self.appliance_type = appliance_type
        self.appliance_brand = appliance_brand
        self.appliance_issue = appliance_issue
        self.date = date
        self.time_frame = time_frame
        self.email = email
        self.phone = phone
        self.dist = dist
        cx_dict[self.cx_name] = self.address, self.appliance_type, self.appliance_brand, self.appliance_issue,\
                                self.date, self.time_frame, self.email, self.phone

    def cx_address(self):
        return self.address

cx_lst = []
cx_1 = Customer("jimmy john", "2303 ballantrae dr, colleyville, texas, 76034", "fridge", "samsung", "no cool", "7/7/20",
                "8-10", None, "123-333-3333")
rick_smith = Customer("Rick Smith", "531 austin st, grapevine, tx 76034", "oven", "LG", "no heat", "6/30/20", "3-5",
                      None, "333-333-3333")
john_doe = Customer("John Doe", "506 Hettie st, Denton, 76209", "Refrigerator", "Samsung", "No cool", "06/25/20", "2-4",
                    "johndoe@aol.com", "222-222-22222")
bill_noff = Customer("Bill Noff", "520 Kay st, argyle, tx, 76226", "washer", "LG", "Leak", "7/21/20", "8-10", None,
                     "000-000-0000")
jack_doe = Customer("Jack Doe", "199 w Jones st, Krum, Tx", "washer", "Samsung", "not spinning", None, None, None, None)
steve_edwards = Customer("Steve Edwards", "4017 Ringdove Way, Roanoke, Tx", "dryer", "Maytag", "no heat", None, None, None, None)
cx_lst.append(cx_1)
cx_lst.append(rick_smith)
cx_lst.append(john_doe)
cx_lst.append(bill_noff)
cx_lst.append(jack_doe)
cx_lst.append(steve_edwards)
Jerry = Technician("Jerry Ploegert", "Denton", "All", 10, "682-321-4068", "502 hettie st, denton, texas", [])
Edwin = Technician("Edwin Palagar", "Denton", "limited", 10, "111-111-1111", "338 Chisholm trl, krum, texas", [])
Dale = Technician("Dale Nester", "Ft Worth", "All", 10, "111-222-3333", "4205 el Campo st, Ft Worth, Texas", [])
addy_lst = []
for cx in cx_lst:
    addy_lst.append(cx.cx_address())
#for cx in cx_lst:
    #if int(str(get_dist(Jerry.home, cx.address)).split(" ")[0]) < int(str(get_dist(Edwin.home, cx.address)).split(" ")[0]) and int(str(get_dist(Jerry.home, cx.address)).split(" ")[0]) < int(str(get_dist(Dale.home, cx.address)).split(" ")[0]):
        #Jerry.cx_list.append(cx.cx_address())
    #elif int(str(get_dist(Edwin.home, cx.address)).split(" ")[0]) < int(str(get_dist(Jerry.home, cx.address)).split(" ")[0]) and int(str(get_dist(Edwin.home, cx.address)).split(" ")[0]) < int(str(get_dist(Dale.home, cx.address)).split(" ")[0]):
        #Edwin.cx_list.append(cx.cx_address())
    #elif int(str(get_dist(Dale.home, cx.address)).split(" ")[0]) < int(str(get_dist(Jerry.home, cx.address)).split(" ")[0]) and int(str(get_dist(Dale.home, cx.address)).split(" ")[0]) < int(str(get_dist(Edwin.home, cx.address)).split(" ")[0]):
        #Dale.cx_list.append(cx.cx_address())
if len(tech_lst) == 1:
    for cx in cx_lst:
        tech_lst[0].cx_lst.append(cx.cx_address())
elif len(tech_lst) == 2:
    for cx in cx_lst:
        if int(str(get_dist(tech_lst[0].home, cx.address)).split(" ")[0]) < int(str(get_dist(tech_lst[1].home, cx.address)).split(" ")[0]):
            tech_lst[0].cx_lst.append(cx.cx_address())
        else:
            tech_lst[1].cx_lst.append(cx.cx_address())
elif len(tech_lst) == 3:
    for cx in cx_lst:
        if int(str(get_dist(tech_lst[0].home, cx.cx_address())).split(" ")[0]) < int(str(get_dist(tech_lst[1].home
                , cx.address)).split(" ")[0]) and int(str(get_dist(tech_lst[0].home, cx.address)).split(" ")[0]) < \
                int(str(get_dist(tech_lst[2].home, cx.address)).split(" ")[0]):
            tech_lst[0].cx_list.append(cx.cx_address())
        elif int(str(get_dist(tech_lst[1].home, cx.cx_address())).split(" ")[0]) < int(str(get_dist(tech_lst[0].home
                , cx.address)).split(" ")[0]) and int(str(get_dist(tech_lst[1].home, cx.address)).split(" ")[0]) < \
                int(str(get_dist(tech_lst[2].home, cx.address)).split(" ")[0]):
            tech_lst[1].cx_list.append(cx.cx_address())
        elif int(str(get_dist(tech_lst[2].home, cx.cx_address())).split(" ")[0]) < int(str(get_dist(tech_lst[0].home
                , cx.address)).split(" ")[0]) and int(str(get_dist(tech_lst[2].home, cx.address)).split(" ")[0]) < \
                int(str(get_dist(tech_lst[1].home, cx.address)).split(" ")[0]):
            tech_lst[2].cx_list.append(cx.cx_address())

def get_lat_long(tech_route):
    loc_long = []
    loc_lat = []
    formatted_addys = []
    results = []
    for location_str in tech_route:
        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address='%s'&key=%s"
                        % (location_str, api_key))
        result = r.json()["results"]
        location = result[0]["geometry"]["location"]
        loc_long.append(location["lng"])
        loc_lat.append(location["lat"])
        formatted_addys.append(result[0]["formatted_address"])
        results.append(result)

    df = pd.DataFrame({"address": tech_route, "latitude": loc_lat, "longitude": loc_long, "formatted_address": formatted_addys})
    waypoints = []
    lat_long = list(zip(loc_lat, loc_long))

    for i in lat_long:
        waypoints.append(str(i).replace(" ", ""))
    waypoints = str(waypoints).replace(", ", "|").replace("(", "").replace(")", "").replace("[", "").replace("]", "")\
        .replace("'", "")


    origin = loc_lat[0], loc_long[0]
    origin = str(origin).replace(" ", "").replace("(", "").replace(")", "")



    destination = loc_lat[-1], loc_long[-1]
    destination = str(destination).replace(" ", "").replace("(", "").replace(")", "")

    start_address = []
    end_address = []
    distance = []
    duration = []

    for i in range(len(waypoints.split("|"))):
        route = ("https://maps.googleapis.com/maps/api/directions/json?language=en-US&units=imperial&origin={}"
                "&destination={}&waypoints=optimize:true|{}&key={}").format(origin, destination, waypoints, api_key)
        route_result = urllib.request.urlopen(route)
        route_result_json = dict(json.loads(route_result.read()))
        distance.append(route_result_json["routes"][0]["legs"][i]["distance"]["text"])
        duration.append(route_result_json["routes"][0]["legs"][i]["duration"]["text"])
        start_address.append(route_result_json["routes"][0]["legs"][i]["start_address"])
        end_address.append(route_result_json["routes"][0]["legs"][i]["end_address"])

    organized_df = pd.DataFrame({"start_address": start_address, "end_address": end_address,
                                "distance": distance, "duration": duration},
                                 columns=["start_address", "end_address", "distance", "duration"])
    optimized_route = str(organized_df["end_address"]).split("Name")[0].strip()



    return str(optimized_route).strip()



for tech in tech_lst:
    print(tech.name + "\n" + get_lat_long(tech.cx_list))


print(Jerry.cx_list)
print(Dale.cx_list)
print(Edwin.cx_list)
print(get_dist(Jerry.home, cx_1.cx_address()))
print(get_dist(Edwin.home, cx_1.cx_address()))
print(get_dist(Dale.home, cx_1.cx_address()))
print("testing commit")
