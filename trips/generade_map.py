import glob
import getorg
from geopy import Nominatim
import csv


geocoder = Nominatim()
location_dict = {}
location = ""
permalink = ""
title = ""

with open('travel.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for i, row in enumerate(csv_reader):
        if i is 0:
        	continue

        print(row)
        location = row[0]
        location_dict[location] = geocoder.geocode(location)
        print(location, "\n", location_dict[location])


m = getorg.orgmap.create_map_obj()
print(getorg.orgmap.output_html_cluster_map(location_dict, folder_name=".", hashed_usernames=False))
