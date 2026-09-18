import csv
from pathlib import Path
from statistics import mean

sec_path = Path(r'/Users/shaunroberts/Desktop/ENVS 5726/SEC_EDGAR_10K')

sec_headers = ['Company Name', 'Year', 'Count Sustainability','Count AI']
sec_table = []

for file_path in sec_path.glob('*'):
    file_name = file_path.name
    name_list = file_path.name.split('-')

    if name_list[0] == 'amzn':
        Company_Name = 'Amazon'
        Year_part = name_list[1][0:4]

    elif name_list[0] == 'goog':
        Company_Name = 'Google'
        Year_part = name_list[1][0:4]

    elif name_list[0] == 'msft':
        Company_Name = 'Microsoft'
        Year_part = name_list[1][4:8]
    else:
        Company_Name = 'Nvidia'
        Year_part = name_list[1][0:4]

    with open(file_path, 'r', encoding='cp1252') as file:
        content = file.read().upper()
    Count_Sustainability = content.count('SUSTAINABILITY')
    Count_AI = content.count('ARITIFICIAL INTELLIGENCE')

    sec_table.append([Company_Name, Year_part, Count_Sustainability, Count_AI])
print(sec_headers)
for row in sec_table:
    print(row)

amazon_metric_table = []
for row in sec_table:
    if row[sec_headers.index('Company Name')] == 'Amazon':
        amazon_metric_table.append(row)

export_csv_path = (Path(r'/Users/shaunroberts/Desktop/ENVS 5726')
    with open(export_csv_path, 'w',newline="", encoding=)
        writer = csv.writer(file)
        writer.writerows([sec_headers]+amazon_metric_table)
