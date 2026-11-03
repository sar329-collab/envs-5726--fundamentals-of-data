from typing import List, Any
from collections import namedtuple

Rohingya_Wash_Survey_Headers: List[str] = [#is there a short cut to do all the ones that start with G?]
Rohingya_Wash_Survey: Type[tuple] = namedtuple(typename='Rohingya_Wash_Survey',field_names=Rohingya_Wash_Survey_Headers)
Rohingya_Wash_Survey_Table: List[tuple] = [
    #something!
]

import sys
sys.path.insert(1, r'/Users/shaunroberts/Desktop/ENVS 5726/week 8/IOM_Rohingya_WASH_Survey.csv')

from datalib import filter_equals

filter_equals(table=Rohingya_Wash_Survey_Table, column_name='Rohingya_Wash_Survey', value=#starts with G)