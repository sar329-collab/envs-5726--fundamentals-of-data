import time
import urllib
import csv
from pathlib import Path
from pprint import pprint
import requests

csv_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 7 /USEIA_Petroleum_Refineries_By_Nearest_Major_City.csv')
Flood_Hazard_Zones_URL = 'https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28/query'

US_Petro_Refineries_table = []
with open(csv_path, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers= next(reader)
    for row in reader:
        US_Petro_Refineries_table.append(row)
headers.append('FEMA Hazard Zone')

for row in US_Petro_Refineries_table:
    Latitude = row[headers.index('Latitude')]
    Longitude = row[headers.index('Longitude')]

geometry = f'{Latitude},{Longitude}'
Query = {
    'geometry': geometry,
    'insR': '4326',
    'geometryType': 'esriGeometryPoint',
    'spatialRel' : 'esriSpatialRelIntersects',
    'outFields': 'ZONE_SUBTY',
    'returnGeometry': 'false',
    'f' : 'pjson'
}

encoded_query = urllib.parse.urlencode(Query)
Flood_Hazard_Zones_URL = Flood_Hazard_Zones_URL + '?' + encoded_query

print(Flood_Hazard_Zones_URL)

try:
    response = requests.get(Flood_Hazard_Zones_URL)
    Flood_Hazard_Zones_data = response.json()
    features = Flood_Hazard_Zones_data['features',[]]

    if features and features[0].get('attributes') is not None:
        zone = features[0]['attributes'].get('Zone_SUBTY')
    else:
        zone = None

    if zone is None or zone == '':
        zone = ('No Data')
except requests.exceptions.ConnectionError:
    time.sleep(5)

    try:
        response = requests.get(Flood_Hazard_Zones_URL)
        Flood_Hazard_Zones_data = response.json()
        features = Flood_Hazard_Zones_data['features',[]]
        if features and features[0].get('attributes') is not None:
            zone = features[0]['attributes'].get('Zone_SUBTY')
        else:
            zone = None
        if zone is None or zone == '':
            zone = ('No Data')
    except requests.exceptions.ConnectionError:
        zone = 'Connection Failed'
row['FEMA Hazard Zone'] = zone
writer.writerow(row)
time.sleep(10)

print(f'{row['Longitude']}, {row['Latitude']}: {zone}')

Flood_Hazard_Zones_data = requests.get(Flood_Hazard_Zones_URL).json()

pprint(Flood_Hazard_Zones_data, width=60)

export_csv_path = (Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 7 /Petro_Hazard_Zones.csv'))
with open(export_csv_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows([headers]+US_Petro_Refineries_table)