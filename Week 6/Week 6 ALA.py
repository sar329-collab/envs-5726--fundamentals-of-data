from pathlib import Path
import csv

hazards_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 6/EJSCREEN_BlockGroup_Hazards.csv')
with open(hazards_path, 'w', newline='', encoding='cp1252') as file:
    writer = csv.writer(file)
    writer.writerows([data_headers]+data_table)

social_vulnerability_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/week 6/EJScreen_BlockGroup_SocialVulnerability.csv')
with open(social_vulnerability_path, 'w', newline='', encoding='cp1252') as file:
    writer = csv.writer(file)
    writer.writerows([data_headers]+data_table)

target_headers=[]
target_table =

join_headers=[]
join_table =

unique_id_name = 'ID_SOCVUL'
target_id_set = set([row[target_headers.index(unique_id_name)] for row in target_table])
join_id_set = set([row[join_headers.index(unique_id_name)] for row in join_table])
