import argparse
import sys
import pyodbc
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
        return headers, rows
    else:
        cursor.commit()
        cursor.close()
        return None, None


def main(category_name: str):
    conn_str = (
        "DRIVER={PostgreSQL Unicode};"
        "SERVER=localhost;"
        "PORT=5432;"
        "DATABASE=Week 11;"
        "UID=postgres;"
        "PWD=0000;"
    )
    conn = pyodbc.connect(conn_str)

    group_by_query = (f'SELECT {category_name}, AVG(mean_ghg_1990_to_2020) '
                      f'FROM epa_ghg GROUP BY {category_name};')
    headers, rows = execute_cursor(conn, sql_query=group_by_query)
    print(headers)
    for row in rows:
        print(row)

    categories = [str(row[0]) for row in rows]
    values = [row[1] for row in rows]

    plt.bar(categories, values)
    plt.title(f'mean_ghg_1990_to_2020 by {category_name}')
    plt.xlabel(category_name)
    plt.ylabel('mean_ghg_1990_to_2020')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    return


def parse_arguments() -> argparse.Namespace:

    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('category_name',
                        type=str,
                        choices=['econ_sector', 'econ_source', 'sector', 'subsector',
                                 'category', 'fuel', 'subcategory1', 'subcategory2',
                                 'subcategory3', 'subcategory4', 'state', 'ghg'],
                        help='The category column to summarize mean_ghg_1990_to_2020 by')
    return parser.parse_args()


if __name__ == '__main__':
    args: argparse.Namespace = parse_arguments()
    sys.exit(
        main(category_name=args.category_name)
    )