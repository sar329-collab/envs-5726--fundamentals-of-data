import urllib
import csv
from pathlib import Path
import requests

csv_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 7 /USEIA_Petroleum_Refineries_By_Nearest_Major_City.csv')
US_Petro_Refineries_headers = ['Latitude','Longitude']

Flood_Hazard_Zones_URL = 'https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28/query'
Flood_Hazard_Zones = requests.get(url=Flood_Hazard_Zones_URL).json()

Flood_Hazard_Zones_headers = ['FEMA Hazard Zone']
US_Petro_Refineries_table = []

with open(csv_path, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    reader([US_Petro_Refineries_headers] + US_Petro_Refineries_table)
    rows = list(reader)

print(Flood_Hazard_Zones_URL)

for row in US_Petro_Refineries_table:
    if  'Latitute' or 'Longitude':
        Query = {
            'geometry': {Latitutde} and {Longitude},
            'insR': '4326',
            'geometryType': 'esriGeometryPoint',
            'spatialRel' : 'esriSpatialRelIntersects',
            'outFields': 'ZONE_SUBTY',
            'returnGeometry': 'false',
            'f' : 'pjson'
         }
        zone
    else:
        zone= None
    if zone is None or == '':
       zone = 'No Data'

US_Petro_Refineries_table.append(row)

encoded_query = urllib.parse.urlencode(query)
Flood_Hazard_Zones_URL = Flood_Hazard_Zones_URL + '?' + encoded_query



