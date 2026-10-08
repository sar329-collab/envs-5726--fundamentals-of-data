import csv

social_vulnerability_table = []
with open(r'/Users/shaunroberts/Desktop/ENVS 5726/week 6/EJScreen_BlockGroup_SocialVulnerability.csv', 'r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    social_vulnerability_header = next(reader)
    for row in reader:
        social_vulnerability_table.append(row)

hazards_table = []
with open(r'/Users/shaunroberts/Desktop/ENVS 5726/week 6/EJSCREEN_BlockGroup_Hazards.csv', 'r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    hazards_header = next(reader)
    for row in reader:
        hazards_table.append(row)

inner_join_target_headers = social_vulnerability_header
inner_join_target_table = social_vulnerability_table

inner_join_join_headers = hazards_header
inner_join_join_table = hazards_table

inner_join_dict = {}
for row in inner_join_join_table:
    unique_id = row[join_header.index(join_id_name)]
    inner_join_dict[unique_id] = [row]

with open(r'/Users/shaunroberts/Desktop/ENVS 5726/week 6/Regression.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(joined_headers)
    writer.writerows(outer_joined_table)