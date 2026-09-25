from pathlib import Path
import json
import csv
import statistics

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

csv_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 5/Cocoa_SupplyChain_Data.csv')

Countries_by_deforestation_dict = {}

with open(csv_path, 'r', encoding='cp1252') as csv_file:
    reader = csv.reader(csv_file)
    data_headers = next(reader)
    for row in reader:
        trader_group, country_of_destination, cocoa_deforestation_15_years_total_exposure, cocoa_net_emissions_15_years_total = row

        if country_of_destination not in Countries_by_deforestation_dict:
            Countries_by_deforestation_dict[country_of_destination] = [float(cocoa_deforestation_15_years_total_exposure)]
        else:
            Countries_by_deforestation_dict[country_of_destination].append(float(cocoa_deforestation_15_years_total_exposure))

export_json_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 5/Countries_by_deforestation')
with open(export_json_path, 'w') as json_file:
    json.dump(Countries_by_deforestation_dict, json_file)

csv_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 5/Cocoa_SupplyChain_Data.csv')

Countries_by_net_emissions_dict = {}

with open(csv_path, 'r', encoding='cp1252') as csv_file:
    reader = csv.reader(csv_file)
    data_headers = next(reader)
    for row in reader:
        trader_group, country_of_destination, cocoa_deforestation_15_years_total_exposure, cocoa_net_emissions_15_years_total = row

        if country_of_destination not in Countries_by_net_emissions_dict:
            Countries_by_net_emissions_dict[country_of_destination] = [float(cocoa_net_emissions_15_years_total)]
        else:
            Countries_by_net_emissions_dict[country_of_destination].append(float(cocoa_net_emissions_15_years_total))

export_json_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 5/Countries_by_net_emissions')
with open(export_json_path, 'w') as json_file:
    json.dump(Countries_by_net_emissions_dict, json_file)

def get_summary_data(summary_dict,):
    summary_table = []
    max_list = []


    for country_of_destination in summary_dict:
        values = summary_dict[country_of_destination]
        total = sum(values)
        max_list.append(total)

    max_sum = max(max_list)
    threshold = max_sum * .1

    for country_of_destination in summary_dict:
        values = summary_dict[country_of_destination]
        total = sum(values)

        if total > threshold:
            summary_table.append([country_of_destination, total])

    return summary_table

summary_deforestation = get_summary_data(Countries_by_deforestation_dict)
summary_emissions = get_summary_data(Countries_by_net_emissions_dict)

export_csv_path = (Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 5/Summary_Deforestation.csv'))
with open(export_csv_path, 'w', newline='', encoding='cp1252') as file:
    writer = csv.writer(file)
    writer.writerows([['Country', 'Deforestation']]+summary_deforestation)

export_csv_path = (Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 5/Summary_Net_Emissions.csv'))
with open(export_csv_path, 'w', newline='', encoding='cp1252') as file:
    writer = csv.writer(file)
    writer.writerows([['Country', 'Emissions']]+summary_emissions)

