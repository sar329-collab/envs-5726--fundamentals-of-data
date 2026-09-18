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
    Count_AI = content.count('ARTIFICIAL INTELLIGENCE')

    sec_table.append([Company_Name, Year_part, Count_Sustainability, Count_AI])
print(sec_headers)
for row in sec_table:
    print(row)

import statistics
def get_average_by_company(headers,table,column_name_to_average, company_name):
    values_to_average= []
    for row in table:
        if row[0] == company_name:
            value = row[headers.index(column_name_to_average)]
            values_to_average.append(value)
    column_average = statistics.mean(values_to_average)
    return column_average

for company_name in ['Nvidia','Microsoft','Google','Amazon']:
    for column_name_to_average in ['Count Sustainability', 'Count AI']:
        column_average = get_average_by_company(headers= sec_headers,
                                                table= sec_table,
                                                column_name_to_average=column_name_to_average,
                                                company_name=company_name)
        print(f'The average of {column_name_to_average} for {company_name} is: {column_average}')

amazon_metric_table = []
for row in sec_table:
    if row[sec_headers.index('Company Name')] == 'Amazon':
        amazon_metric_table.append(row)

export_csv_path = (Path(r'/Users/shaunroberts/Desktop/ENVS 5726/SEC_10k_Amazon_Metrics.csv'))
with open(export_csv_path, 'w', newline='', encoding='cp1252') as file:
    writer = csv.writer(file)
    writer.writerows([sec_headers]+amazon_metric_table)

google_metric_table = []
for row in sec_table:
    if row[sec_headers.index('Company Name')] == 'Google':
        google_metric_table.append(row)

export_csv_path = (Path(r'/Users/shaunroberts/Desktop/ENVS 5726/SEC_10k_Google_Metrics.csv'))
with open(export_csv_path, 'w', newline='', encoding='cp1252') as file:
    writer = csv.writer(file)
    writer.writerows([sec_headers]+google_metric_table)

Microsoft_metric_table = []
for row in sec_table:
    if row[sec_headers.index('Company Name')] == 'Microsoft':
        Microsoft_metric_table.append(row)

export_csv_path = (Path(r'/Users/shaunroberts/Desktop/ENVS 5726/SEC_10k_Microsoft_Metrics.csv'))
with open(export_csv_path, 'w', newline='', encoding='cp1252') as file:
    writer = csv.writer(file)
    writer.writerows([sec_headers]+Microsoft_metric_table)

Nvidia_metric_table = []
for row in sec_table:
    if row[sec_headers.index('Company Name')] == 'Nvidia':
        Nvidia_metric_table.append(row)

export_csv_path = (Path(r'/Users/shaunroberts/Desktop/ENVS 5726/SEC_10k_Nvidia_Metrics.csv'))
with open(export_csv_path, 'w', newline='', encoding='cp1252') as file:
    writer = csv.writer(file)
    writer.writerows([sec_headers]+Nvidia_metric_table)