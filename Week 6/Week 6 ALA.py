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

target_header = social_vulnerability_header
target_table = social_vulnerability_table

join_header = hazards_header
join_table = hazards_table

target_id_name = 'ID_SOCVUL'
join_id_name = 'ID_HAZ'

one_to_many_join_dict = {}

for row in join_table:
    join_id = row[join_header.index(join_id_name)]
    if join_id not in one_to_many_join_dict:
        one_to_many_join_dict[join_id] = [row]
    else:
        one_to_many_join_dict[join_id].append(row)

joined_headers = target_header + join_header
outer_joined_table = []

for target_row in target_table:
    target_id = target_row[target_header.index(target_id_name)]
    if target_id in one_to_many_join_dict:
        for join_row in one_to_many_join_dict[target_id]:
            outer_joined_table.append(target_row + join_row)
    else:
        join_row = [None] * len(join_header)
        outer_joined_table.append(target_row + join_row)

target_id_set = set([row[target_header.index(target_id_name)] for row in target_table])

for join_id in one_to_many_join_dict:
    if join_id not in target_id_set:
        for join_row in one_to_many_join_dict[join_id]:
            target_row = [None] * len(target_header)
            outer_joined_table.append(target_row + join_row)

with open(r'/Users/shaunroberts/Desktop/ENVS 5726/week 6/Full_Outer_Join.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(joined_headers)
    writer.writerows(outer_joined_table)


join_id_set = set([row[join_header.index(join_id_name)] for row in join_table])
intersection_set = target_id_set.intersection(join_id_set)
intersection = len(intersection_set)
union_set = target_id_set.union(join_id_set)
union = len(union_set)
print(f'There are {intersection} inner joined rows of {union} total Block Groups')


