

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks.
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy

import glob
import getorg
from geopy import Nominatim
import csv
g = glob.glob("*.md")


geocoder = Nominatim()
location_dict = {}
location = ""
permalink = ""
title = ""


# for file in g:
#     with open(file, 'r') as f:
#         lines = f.read()
#         if lines.find('location: "') > 1:
#             loc_start = lines.find('location: "') + 11
#             lines_trim = lines[loc_start:]
#             loc_end = lines_trim.find('"')
#             location = lines_trim[:loc_end]
#             print(location)


with open('../travel.csv') as csv_file:
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
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="../trips", hashed_usernames=False)




