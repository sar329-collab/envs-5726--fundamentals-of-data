import time
import urllib
import csv
from pathlib import Path
import requests
from pprint import pprint

csv_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 7 /USEIA_Petroleum_Refineries_By_Nearest_Major_City.csv')
Flood_Hazard_Zones_URL = 'https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28/query'
OSRM_URL = 'https://map.project-osrm.org/'

US_Petro_Refineries_table = []
with open(csv_path, 'r', newline='', encoding='cp1252') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        US_Petro_Refineries_table.append(row)
headers.append('FEMA Hazard Zone'+'Drive Duration Seconds')

for row in US_Petro_Refineries_table:
    Nearest_City_Latitude = row[headers.index('NearestMajorCity_Latitude')]
    Nearest_City_Longitude = row[headers.index('NearestMajorCity_Longitude')]
    Latitude = row[headers.index('Latitude')]
    Longitude = row[headers.index('Longitude')]
    count = count + 1
    print(f'working on {count}')

    nearest_major_city = f'{Nearest_City_Longitude},{Nearest_City_Latitude}'
    origin = f'{Longitude},{Latitude}'
    Query = {

    }

    encoded_query = urllib.parse.urlencode(Query)
    Drive_URL = OSRM_URL + '?' + encoded_query