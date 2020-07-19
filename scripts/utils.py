import json
import sys
import os

def check_region(regions):
    data_countries = {}
    file_path = os.path.dirname(os.path.realpath(__file__))
    with open(file_path + '/countries.json', 'r') as f:
        data_countries = json.load(f)

    for reg in regions:
        if reg not in data_countries:
            print(f'Error: {reg} not a region')
            sys.exit()
