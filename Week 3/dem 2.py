def is_min_ratio_toilets_to_people_met(ratio_of_toilets):
    ratio_of_toilets=ratio_of_toilets.split('/')
    toilets=int(ratio_of_toilets[0].replace( 't'," "))
    people=int(ratio_of_toilets[1].replace('p'," "))
    ratio_of_toilets = toilets/people
    if ratio_of_toilets >= 1/20:
        return True
    else:
        return False
print(is_min_ratio_toilets_to_people_met('1t/37p'))
print(is_min_ratio_toilets_to_people_met('1t/12p'))

def is_population_disabled(disabled, population):
    ratio = disabled / population
    if ratio > 1/10:
        return True
    else:
        return False
print(is_population_disabled(0, 52))
print(is_population_disabled(52, 392))

def is_gp_religious_or_academic(gp):
    religious_list = ['mosque','church']
    religious_set = set(religious_list)
    academic_list = ['school', 'institution','faculty']
    academic_set = set(academic_list)

    if religious_set or academic_set in gp:
        return True
    else:
        return False

print(is_gp_religious_or_academic('faculty of earth sciences and mining'))
print(is_gp_religious_or_academic('almorada chruch'))
print(is_gp_religious_or_academic('health insulation building'))

def get_sanitation_priority(ratio, disabled, pop, gp):


print(get_sanitation_priority(ratio='1t/49p', disabled=2, pop=392, gp='Faculty - Student Dwelling'))
print(get_sanitation_priority(ratio='1t/29p', disabled=0, pop=178, gp='Mohamed Ali Abbas Secondary School for Girls'))
print(get_sanitation_priority(ratio='1t/17p', disabled=0, pop=52, gp='Alsalem Old Mosque'))
print(get_sanitation_priority(ratio='1t/6p', disabled=0, pop=12, gp='Nile Club'))

