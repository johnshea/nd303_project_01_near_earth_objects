"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
import helpers


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output
    row corresponds to the information in a single close approach from the
    `results` stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be
        saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    with open(filename, 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fieldnames)

        for row in results:
            result_dict = {field: None for field in fieldnames}

            result_dict['datetime_utc'] = helpers.datetime_to_str(row.time)
            result_dict['distance_au'] = row.distance
            result_dict['velocity_km_s'] = row.velocity
            result_dict['designation'] = row.neo.designation

            if result_dict['name'] is None:
                result_dict['name'] = ''

            if row.neo.diameter == float('nan'):
                result_dict['diameter_km'] = 'nan'
            else:
                result_dict['diameter_km'] = row.neo.diameter

            result_dict['potentially_hazardous'] = row.neo.hazardous

            writer.writerow(result_dict.values())


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is
    a list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be
        saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'neo')

    data = []

    for row in results:
        result_dict = {field: None for field in fieldnames}

        result_dict['datetime_utc'] = helpers.datetime_to_str(row.time)
        result_dict['distance_au'] = row.distance
        result_dict['velocity_km_s'] = row.velocity

        neo_dict = {
            'designation': None, 'name': None,
            'diameter_km': None, 'potentially_hazardous': None
        }

        neo_dict['designation'] = row.neo.designation

        if row.neo.name is None:
            neo_dict['name'] = ''
        else:
            neo_dict['name'] = row.neo.name

        if row.neo.diameter == float('nan'):
            neo_dict['diameter_km'] = float('nan')
        else:
            neo_dict['diameter_km'] = row.neo.diameter

        neo_dict['potentially_hazardous'] = row.neo.hazardous

        result_dict['neo'] = neo_dict

        data.append(result_dict)

    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
