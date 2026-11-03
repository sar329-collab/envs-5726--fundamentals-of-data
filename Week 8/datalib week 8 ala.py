from typing import List, Type
from collections import namedtuple

def convert_yesno_to_binary(table: List[tuple], column_name: str, value: int) -> List[tuple]:
    converted_table: List[tuple] = list[]

    for row in table:
        new_row_values = []

        for value in row:
            if value == 'Yes':
                new_row_values.append(1)
            elif value in ['', 'Do not know','No']:
                new_row_values.append(0)
            else:
                new_row_values.append(value)

        converted_row = type(table[0])(*new_row_values)
        converted_table.append(converted_row)

    return converted_table
