from collections import namedtuple
from pathlib import Path
from openpyxl import load_workbook
from scipy.optimize import curve_fit
import numpy as np
from typing import NamedTuple
import datetime
import csv

pipe_material_training_data_xlsx_path = r'/Users/shaunroberts/Desktop/ENVS 5726/week 9/Pipe_Material_Training_Data.xlsx'

workbook = load_workbook(pipe_material_training_data_xlsx_path)
sheet = workbook['Survival Probabilities']

pipe_materials_table = []

headers = [cell.value for cell in next(sheet.iter_rows())]

for row in sheet.iter_rows(min_row=2):
    pipe_materials_table.append([cell.value for cell in row])

csv_path = '/Users/shaunroberts/Desktop/ENVS 5726/week 9/Water_Mains.csv'
water_mains_table = []

with open(csv_path, 'r', newline='', encoding='cp1252') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        water_mains_table.append(row)
headers.append('Age')
headers.append('Survival_Probability')

class water_mains(NamedTuple):
    MainType: str
    Diameter: int
    InstallDate: datetime.datetime
    Material: str

for row in water_mains_table:
    print(row)