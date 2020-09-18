#!/usr/bin/env python3

NEFarm = {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]}
WFarm = {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}
SEFarm = {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}

farms = []

farms.append(NEFarm)
farms.append(WFarm)
farms.append(SEFarm)

## Can only get to work with one dict
#for k, v in NEFarm.items():
#    print(k, v)

#print(farms)

for farm in farms:
    print(f"{farm['name']} raises {', '.join(farm['agriculture'])}.")





