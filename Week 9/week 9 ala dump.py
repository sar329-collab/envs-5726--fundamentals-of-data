from pathlib import Path
import csv
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from scipy.optimize import curve_fit
import numpy as np

pipe_material_training_data_xlsx_path = r'/Users/shaunroberts/Desktop/ENVS 5726/week 9/Pipe_Material_Training_Data.xlsx'

workbook = load_workbook(pipe_material_training_data_xlsx_path)
sheet = workbook['Survival Probabilities']

pipe_materials_table = []

headers = [cell.value for cell in next(sheet.iter_rows())]

for row in sheet.iter_rows(min_row=2):
    pipe_materials_table.append([cell.value for cell in row])

def cumulative_density_function(age, c, b, a):
    return 1-c*np.exp(-(age/b)**a)

def plot_cdf_curve_fit(table, material_type, line_color):
    xdata = [
        row[headers.index('Life Expectancy (y)')]
        for row in table
        if row[headers.index('Material Type')] == material_type
    ]
    ydata = [
        row[headers.index('Surv. Prob. (%)')]
        for row in table
        if row[headers.index('Material Type')] == material_type
    ]

    coefficients, bounds = curve_fit(cumulative_density_function, xdata, ydata)
    c,b,a = coefficients
    print(f'Curve fitted CDF for {material_type}: Survival Probability = {c}*e^ (-(age/{b})^{a})')

    x = list(range(1,151))
    y = [cumulative_density_function(age, c, b, a) for age in x]
    plt.plot(x, y, color=line_color, label=material_type)

    return float(c), float(b), float(a)

plot_cdf_curve_fit(table=pipe_materials_table, material_type='Cast Iron', line_color='red')
plot_cdf_curve_fit(table=pipe_materials_table, material_type='Ductile Iron', line_color='blue')
plot_cdf_curve_fit(table=pipe_materials_table, material_type='Galvanized Iron', line_color='green')
plot_cdf_curve_fit(table=pipe_materials_table, material_type='Copper', line_color='brown')
plt.legend()
plt.xlabel('Life Expectancy (y)')
plt.ylabel('Survival Probability (%)')
plt.title('Pipe Material Survival CDF')
plt.show