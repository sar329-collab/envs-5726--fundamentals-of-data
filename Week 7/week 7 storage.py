from pprint import pprint
import urllib
import requests
import csv
from pathlib import Path

csv_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 7 /USEIA_Petroleum_Refineries_By_Nearest_Major_City.csv')

US_Petro_Refineries_dict = {
    'Latitude' : []
    'Longitude': []
}
with open(r'/Users/shaunroberts/Desktop/ENVS 5726/week 7 /USEIA_Petroleum_Refineries_By_Nearest_Major_City.csv','r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    US_Petro_Refineries_header = next(reader)
    for row in reader:
        for column_name in US_Petro_Refineries_dict:
            Refinery = float(row[US_Petro_Refineries_header[column_name]])
            US_Petro_Refineries_dict[column_name].append(Refinery)

fema_hazard_zones_url = 'https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28/query'

query = {
    'geometry': 'Latitutde' 'Longitude' '
    'insR': '4326',
    'geometryType': 'esriGeometryPoint',
    'spatialRel' : 'esriSpatialRelIntersects',
    'outFields': 'ZONE_SUBTY',
    'returnGeometry': 'false',
    'f' : 'pjson'
}

encoded_query = urllib.parse.urlencode(query)
fema_hazard_zones_url = fema_hazard_zones_url + '?' + encoded_query

fema_hazard_zones_data = requests.get(url = fema_hazard_zones_url).json()