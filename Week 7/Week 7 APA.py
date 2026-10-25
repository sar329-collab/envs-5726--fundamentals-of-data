import time
import urllib
import csv
from pathlib import Path
import requests
from pprint import pprint
#task 1 and 4 set up
csv_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 7 /USEIA_Petroleum_Refineries_By_Nearest_Major_City.csv')
Flood_Hazard_Zones_URL = 'https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28/query'
OSRM_URL = 'https://routing.openstreetmap.de/routed-car/route/v1/driving/'

US_Petro_Refineries_table = []
with open(csv_path, 'r', newline='', encoding='cp1252') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        US_Petro_Refineries_table.append(row)
headers.append('FEMA Hazard Zone')
headers.append('Drive Duration')

count = 0
for row in US_Petro_Refineries_table:
    Latitude = row[headers.index('Latitude')]
    Longitude = row[headers.index('Longitude')]
    Nearest_City_Latitude = row[headers.index('NearestMajorCity_Latitude')]
    Nearest_City_Longitude = row[headers.index('NearestMajorCity_Longitude')]
    zone = 'No Data'
    duration = 'No Data'
    count = count + 1
    print(f'working on {count}')
    #task 1 - fema hazard
    geometry = f'{Longitude},{Latitude}'
    Query = {
        'geometry': geometry,
        'inSR': '4326',
        'geometryType': 'esriGeometryPoint',
        'spatialRel': 'esriSpatialRelIntersects',
        'outFields': 'ZONE_SUBTY',
        'returnGeometry': 'false',
        'f': 'pjson'
    }
    #task 4 - driving distance
    origin = geometry
    destination = f'{Nearest_City_Longitude},{Nearest_City_Latitude}'
    route_url = OSRM_URL + origin + ';' + destination
    OSRM_Query = {
        'steps': 'false',
        'alternatives': 'true',
        'overview': 'false'
    }

    #task 1 - fema hazard
    encoded_query = urllib.parse.urlencode(Query)
    Row_URL = Flood_Hazard_Zones_URL + '?' + encoded_query

    try:
        Response = requests.get(url = Row_URL)
        Flood_Hazard_Zones_data = Response.json()
        features = Flood_Hazard_Zones_data.get('features', [])

        if features and features[0].get('attributes') is not None:
                zone = features[0]['attributes'].get('ZONE_SUBTY')
        else:
            zone

    except (requests.exceptions.ConnectionError, ValueError, KeyError):
        time.sleep(5)

        try:
            Response = requests.get(url = Row_URL)
            Flood_Hazard_Zones_data = Response.json()
            features = Flood_Hazard_Zones_data.get('features', [])

            if features and features[0].get('attributes') is not None:
                zone = features[0]['attributes'].get('ZONE_SUBTY')
            else:
                zone
        except (requests.exceptions.ConnectionError, ValueError, KeyError):
            zone = 'Connection Failed'

    row.append(zone)

    #task 4 - drive duration
    Encoded_OSRM_Query = urllib.parse.urlencode(OSRM_Query)
    OSRM_Query_URL = route_url + '?' + Encoded_OSRM_Query

    try:
        Response = requests.get(url=OSRM_Query_URL)
        route_data = Response.json()
        routes = route_data.get('routes', [])

        if routes:
            duration = routes[0]['duration']
        else:
            duration
    except (requests.exceptions.ConnectionError, ValueError, KeyError):
        time.sleep(5)

        try:
            Response = requests.get(url=OSRM_Query_URL)
            route_data = Response.json()
            routes = route_data.get('routes', [])

            if routes:
                duration = routes[0]['duration']
            else:
                duration
        except (requests.exceptions.ConnectionError, ValueError, KeyError):
            zone = 'Connection Failed'

    print(OSRM_Query_URL)
    row.append(duration)
    time.sleep(10)

export_csv_path = (Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 7 /Petro_Hazard_Zones_FEMA_Drive_Duration.csv'))
with open(export_csv_path, 'w', newline='', encoding='cp1252') as file:
    writer = csv.writer(file)
    writer.writerows([headers]+US_Petro_Refineries_table)
print('My script finished')