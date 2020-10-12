# This script plots input data and prints it to a PNG file.

"""
INPUTS
    A list of lists (preferably one from data_loader or similar)
OUTPUTS
    A PNG file. If run directly, it outputs the graph to console as well.
"""

import numpy as np
import matplotlib.pyplot as plt
from data_loader import data_loader

def data_plotter(dataset):
    # Break the input into its respective variables
    x = [i[1] for i in dataset] 
    y = [i[1] for i in dataset] 
    plt.plot(x, y, 'o', color='black')
    plt.show()


datas = data_loader()
data_plotter(datas)