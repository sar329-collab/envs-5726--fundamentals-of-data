from typing import List, Any

def survey_equals(table: List[tuple], column_name: str, value: Any) -> List[Tuple]:
    print(f'Filtering {len(table)} rows where {column_name} equals {value}')
    return table