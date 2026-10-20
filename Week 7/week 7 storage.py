import time
import urllib
import csv
from pathlib import Path
import requests

csv_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 7 /USEIA_Petroleum_Refineries_By_Nearest_Major_City.csv')
Flood_Hazard_Zones_URL = 'https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28/query'

US_Petro_Refineries_table = []
with open(csv_path, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        US_Petro_Refineries_table.append(row)
headers.append('FEMA Hazard Zone')

count = 0
for row in US_Petro_Refineries_table:
    Latitude = row[headers.index('Latitude')]
    Longitude = row[headers.index('Longitude')]
    zone = 'No Data'
    count = count + 1
    print(f'working on {count}')

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
    Row_URL = Flood_Hazard_Zones_URL + '?' + encoded_query

    try:
        Response = requests.get(url = Row_URL)
        Flood_Hazard_Zones_data = Response.json()
        features = Flood_Hazard_Zones_data.get('features', [])

        if features and features[0].get('attributes') is not None:
                zone = features[0]['attributes'].get('ZONE_SUBTY')
            else:
                zone = None

    except requests.exceptions.ConnectionError:
        time.sleep(5)

        try:
            Response = requests.get(url = Row_URL)
            Flood_Hazard_Zones_data = Response.json()
            features = Flood_Hazard_Zones_data.get('features', [])

            if features and features[0].get('attributes') is not None:
                zone = features[0]['attributes'].get('ZONE_SUBTY')
            else:
                zone = None
        except requests.exceptions.ConnectionError:
            zone = 'Connection Failed'

    row.append(zone)
    time.sleep(10)

export_csv_path = (Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 7 /Petro_Hazard_Zones.csv'))
with open(export_csv_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows([headers]+US_Petro_Refineries_table)

print('My script finished')