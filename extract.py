"""Extract data on near-Earth objects and approaches from files(CSV,JSON).

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth
        objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []

    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            neo = NearEarthObject(**row)
            neos.append(neo)

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close
        approaches.
    :return: A collection of `CloseApproach`es.
    """
    close_approaches = []

    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)
        fields = contents['fields']
        for item in contents['data']:
            close_approach_dict = dict(zip(fields, item))

            close_approach = CloseApproach(**close_approach_dict)
            close_approaches.append(close_approach)

    return close_approaches
