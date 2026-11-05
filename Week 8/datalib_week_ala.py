from typing import List, Type
from collections import namedtuple

def convert_yesno_to_binary(table: List[tuple]) -> List[tuple]:
    RowClass: Type[tuple] = type(table[0])

    converted_table: List[tuple] = []

    for row in table:
        new_row_values = []

        for value in row:
            if value == 'Yes':
                new_row_values.append(1)
            elif value in ['', 'Do not know','No']:
                new_row_values.append(0)
            else:
                new_row_values.append(value)

        converted_row = RowClass(*new_row_values)
        converted_table.append(converted_row)

    return converted_table

def convert_values_to_numeric(table: list[tuple]) -> list[tuple]:
    NamedTupleClass = type(table[0])
    master_dictionary = {}

    for column_name in NamedTupleClass._fields:
        column_dictionary = {}

        for row in table:
            value = getattr(row, column_name)

            if type(value) == str:
                if value not in column_dictionary:
                    column_dictionary[value] = len(column_dictionary) + 1

        master_dictionary[column_name] = column_dictionary

    converted_table = []

    for row in table:
        new_row_values = []

        for column_name in NamedTupleClass._fields:
            value = getattr(row, column_name)

            if type(value) == str:
                new_value = master_dictionary[column_name][value]
                new_row_values.append(new_value)
            else:
                new_row_values.append(value)

        converted_row = NamedTupleClass(*new_row_values)
        converted_table.append(converted_row)

        return converted_table
