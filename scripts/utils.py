import json
import sys

def check_region(regions):
    data_countries = {}
    with open('countries.json', 'r') as f:
        data_countries = json.load(f)

    for reg in regions:
        if reg not in data_countries:
            print(f'Error: {reg} not a region')
            sys.exit()
