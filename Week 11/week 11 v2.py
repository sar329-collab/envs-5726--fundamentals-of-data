import pyodbc
import argparse
import sys
import matplotlib.pyplot as plt

def execute_cursor(conn, sql_query: str) -> tuple:
    print(f'Executing query: {sql_query}')
    cursor = conn.cursor()
    cursor.execute(sql_query)
    if 'SELECT' in sql_query:
        rows = cursor.fetchall()
        headers = [column[0] for column in cursor.description]
        cursor.commit()
        cursor.close()
        return rows, headers
    else:
        cursor.commit()
        cursor.close()
        return None, None

def main(category_name: str, value_column: str, statistic: str):
    conn_str = (
        "DRIVER={PostgreSQL Unicode};"
        "SERVER=localhost;"
        "PORT=5432;"
        "Database=week_11_database;"
        "UID=postgres;"
        "PWD=data;"
    )
    conn = pydoc.connect(conn_str)

    group_by_query = (f'SELECT {category_name}, {statistic}({value_column})'
                      f'FROM epa_ghg_1990s and epa_ghg_2000s GROUP BY {category_name};')
    headers, rows = execute_cursor(conn=conn, sql_query=group_by_query)
    print(headers)
    for row in rows:
        print(row)
    return

def parse_arguements() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('category_name', type=str, choices=['ROWNUMBER'])
    parser.add_argument('value_column', type=str, choices=['mean_ghg_1990_to_2020'])
    parser.add_argument('statistic', type=str, choices=['AVG'])
    return parser.parse_args()

if __name__ == '__main__':
    args: argparse.Namespace = parse_arguements()
    sys.exit(
        main(category_column=args.category_column,
             value_column=args.value_column,
             statistic=args.statistic)
    )

bin_width = 1
bins=range(min('mean_ghg_1990_to_2020'), max('mean_ghg_1990_to_2020') + bin_width, bin_width)

plt.hist('mean_ghg_1990_to_2020', bins=bins,color='blue')
plt.xlabel('sector')
plt.ylabel('mean_ghg_1990_to_2020')
plt.title('mean_ghg_1990_to_2020 by sector')
print('mean_ghg_1990_to_2020 by sector')
