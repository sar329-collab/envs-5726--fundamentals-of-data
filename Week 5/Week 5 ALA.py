from pathlib import Path
import json

json_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/Trase_CIV_Cocoa_SupplyChain_Data.json')

with open(json_path) as f:
    data = json.load(f)
    for record in data['cote_divoire_cocoa_v1_1_1']['data']:
        record['supply_chain_data']['trader_group']
        print(record['supply_chain_data']['trader_group'])

data_headers = ['trader_group', 'country_of_destination','cocoa_deforestation_15_years_total_exposure', 'cocoa_net_emissions_15_years_total']
data_table = []
for record in data:
    print(record)

    data_values = [record[header] for header in data_headers]
    data_table.append(data_values)

print(data_table)
for row in data_table:
    print(row)