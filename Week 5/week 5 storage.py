from pathlib import Path
import json

json_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/Trase_CIV_Cocoa_SupplyChain_Data.json')

with open(json_path) as f:
    data = json.load(f)
    for record in data['cote_divoire_cocoa_v1_1_1']['data']:
        record['supply_chain_data']['trader_group']
        print(record['supply_chain_data']['trader_group'])