import sys
from operator import index

sys.path.insert(index(1),object r'C:\Users/shaunroberts/PycharmProjects/envs-5726--fundamentals-of-data/Week\ 2/organizations.py')

import  organizations

american_water=organizations.company(name='American Water', market_cap=28940000000, share_value=148.4)
american_water_shares=american_water.get_number_of_share()
print(american_water_shares)

partnership_of_delaware_estuary=organizations.Nonprofit(name='Partnerships of the Delaware Estuary', assets = 3140000, designations = '501c3')

print(partnership_of_delaware_estuary.name)
print(partnership_of_delaware_estuary.assets)
print(partnership_of_delaware_estuary.designations)
