#task 1 - converting list into named tuples
import csv
from collections import namedtuple
from operator import index
from pathlib import Path

csv_path= '/Users/shaunroberts/Desktop/ENVS 5726/week 8/IOM_Rohingya_WASH_Survey_2.csv'
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

#task 4
import pandas as pd
from factor_analyzer import FactorAnalyzer

data = pd.DataFrame.from_records(data=final_converted_table, columns=final_converted_table[0]._fields)

fa = FactorAnalyzer(rotation="varimax")
#fa.fit(data)

#task 5
corr = data.corr()
print(corr)

constant_columns = data.columns[data.nunique() == 1]
print(constant_columns.tolist())

data_clean = data.drop(columns=constant_columns)
print(data_clean)

#TASK 6 - create factor analysis object & factor analysis
from factor_analyzer import FactorAnalyzer

#perform factor analysis with determined number of factors
number_of_factors = 5
fa = FactorAnalyzer(n_factors=number_of_factors, rotation="varimax")
fa.fit(data_clean)

factor_names = [f'Factor{i+1}' for i in range(number_of_factors)]

loadings_df = pd.DataFrame(fa.loadings_, columns=factor_names, index=data_clean.columns)

#get variance of each factor
index_names = ['sum of squared loadings', 'proportional variance','cumulative variance']
variance_df = pd.DataFrame(fa.get_factor_variance(), columns=factor_names, index=index_names)

loadings_df.to_csv(r'/Users/shaunroberts/Desktop/ENVS 5726/week 8/IOM_Rohingya_WASH_Loading.csv')
variance_df.to_csv(r'/Users/shaunroberts/Desktop/ENVS 5726/week 8/IOM_Rohingya_WASH_Variance.csv')




