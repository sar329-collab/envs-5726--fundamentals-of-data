#task 1 - converting list into named tuples
import csv
from collections import namedtuple
from operator import index
from pathlib import Path

csv_path= '/Users/shaunroberts/Desktop/ENVS 5726/week 8/IOM_Rohingya_WASH_Survey.csv'
survey_record_table= []

with open(csv_path, newline='', encoding='cp1252') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)

    g_headers= [header for header in headers if header.startswith('G')]

    SurveyRecord = namedtuple('SurveyRecord', field_names=g_headers)

    for row in reader:
        g_row_values = [row[headers.index(column)] for column in g_headers]

        Survey_Record = SurveyRecord(*g_row_values)
        survey_record_table.append(Survey_Record)
print(survey_record_table[0])

#task 2 - Execution Script Binary Function
import sys
sys.path.insert(1, '/Users/shaunroberts/Desktop/ENVS 5726')
from datalib_week_ala import convert_yesno_to_binary

binary_survey_table = convert_yesno_to_binary(table=survey_record_table)

print(binary_survey_table[0])

#task 3 - Execution Script Values to Numeric

from datalib_week_ala import convert_yesno_to_binary, convert_values_to_numeric

binary_survey_table = convert_yesno_to_binary(survey_record_table)
final_converted_table = convert_values_to_numeric(binary_survey_table)

print(final_converted_table[0])

#task 4 and 5 - factor analysis
import pandas as pdp
from factor_analyzer import FactorAnalyzer
fa = FactorAnalyzer(rotation="varimax")
fa.fit(data)




