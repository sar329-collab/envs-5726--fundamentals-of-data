from pathlib import Path
import json
import csv

json_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/Trase_CIV_Cocoa_SupplyChain_Data.json')

with open(json_path) as f:
    data = json.load(f)

data_headers = ['trader_group', 'country_of_destination','cocoa_deforestation_15_years_total_exposure', 'cocoa_net_emissions_15_years_total']
data_table = []
for record in data['cote_divoire_cocoa_v1_1_1']['data']:
    trader_group = record['supply_chain_data']['trader_group']
    country_of_destination = record['supply_chain_data']['country_of_destination']
    cocoa_deforestation_15_years_total_exposure = record['cocoa_data']['cocoa_deforestation_15_years_total_exposure']
    cocoa_net_emissions_15_years_total =record['cocoa_data']['cocoa_net_emissions_15_years_total']
    data_table.append([trader_group,country_of_destination,cocoa_deforestation_15_years_total_exposure,cocoa_net_emissions_15_years_total])

print(data_table)
for row in data_table:
    print(row)

export_csv_path = (Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 5/Cocoa_SupplyChain_Data.csv'))
with open(export_csv_path, 'w', newline='', encoding='cp1252') as file:
    writer = csv.writer(file)
    writer.writerows([data_headers]+data_table)