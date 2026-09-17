file_headers = ['Company Name', 'Year', 'Count Sustainability','Count AI']
file_table = []
for file_path in folder_path.glob('*'):
    file_name = file_path.name
    file_extention = file_name.split('.')[-1]
    file_table.append([str(file_path), file_name, file_extention])

print(file_headers)
for row in file_table:
    print(row)