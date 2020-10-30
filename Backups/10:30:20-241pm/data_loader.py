# This script loads the data from KIC 201325107 for Model.csv
# And returns the data as two lists.

"""
INPUTS
    None
OUTPUTS
    A list of lists of the data from the csv
"""

import csv

def data_loader():
    with open('KIC 201325107 for Model.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    return data