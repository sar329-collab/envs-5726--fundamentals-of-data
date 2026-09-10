import statistics
import datetime
def is_min_ratio_toilets_to_people_met(ratio_of_toilets):
    if ratio_of_toilets >= 1/20:
        return True
    else:
        return False
print(is_min_ratio_toilets_to_people_met('1t/37p'))
print(is_min_ratio_toilets_to_people_met('1t/12p'))# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def is_population_disabled(disabled, total_population):
  return disabled / total_population
if(is_population_disabled)< .10:
    return ("False")
if(is_population_disabled)> .10:
    return ("True")
print(is_population_disabled(disabled=0, total_population=32))
print(is_population_disabled(disabled=52, total_population=392))