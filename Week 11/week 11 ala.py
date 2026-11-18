import pydoc
import argparse
import sys

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

def main(category_column: str, value_column: str, statistic: str):
    conn_str = (
        "DRIVER={PostgreSQL Database Version};"
        "SERVER=localhost;"
        "PORT=5432;"
        "Database=week_11_database;"
        "UID=postgres;"
        "PWD=data;"
    )
    conn = pydoc.connect(conn_str)

    group_by_query = (f'SELECT {category_column}, {statistic}({value_column})'
                      f'FROM epa_ghg_1990s and epa_ghg_2000s GROUP BY {category_column};')
    headers, rows = execute_cursor(conn=conn, sql_query=group_by_query)
    print(headers)
    for row in rows:
        print(row)
    return

def parse_arguements() -> argparse.Namespace:
    #left off