"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, 'r') as f:
        reader = csv.DictReader(f)
        neos = [
            NearEarthObject(
                designation=row['pdes'],
                name=row['name'] if row['name'] else None,
                diameter=float(row['diameter']) if row['diameter'] else float('nan'),
                hazardous=False if row['pha'] in ["", "N"] else True
            ) for row in reader
        ]
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    
    with open(cad_json_path, 'r') as f:
        data = json.load(f)
    
        fields = data['fields']
        ca_data = data['data']
        
        # Create a dictionary for field indices
        field_indices = {field: index for index, field in enumerate(fields)}
        
        approaches = [
            CloseApproach(
                designation=row[field_indices['des']],
                time=row[field_indices['cd']],
                distance=float(row[field_indices['dist']]),
                velocity=float(row[field_indices['v_rel']])
            ) for row in ca_data
        ]
    
    return approaches
