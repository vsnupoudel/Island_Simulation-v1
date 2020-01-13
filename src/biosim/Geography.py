# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse; Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import numpy as np
import textwrap
# import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from biosim.Mapping import Jungle, Savannah, Desert, Ocean, Mountain


class Geo:
    """
    - Stores the size/shape of the geography
    - Converts string input of map into a 2D matrix of Objects
    - Objects can be only one of the five Landscape types
    """
    valid_list = ['O', 'S', 'D', 'J', 'M']

    def __init__(self, geo_matrix_input_string):
        """
        - Check if input characters are valid letters
        - Check if all rows in map have equal length
        - Check that ocean O is around all edges of map
        :param geo_matrix_input_string: String with map coordinates
        """
        self.geo_graph = textwrap.dedent(geo_matrix_input_string)
        self.lines = self.geo_graph.splitlines()  # string into lines

        # check if input characters are valid letters
        for line in self.lines:
            for letter in line:
                if letter not in self.valid_list:
                    raise ValueError(" Invalid Letters in the Input map ")

        self.geo_list = [list(_) for _ in self.lines]  # each letter separated
        self.geo_shape = np.shape(self.geo_list)

        # Check if all rows in map have equal length
        # No need to check for columns
        self.length_first = len(self.lines[0])
        for line in self.lines:
            if len(line) != self.length_first:
                raise ValueError("The length of rows not equal")

        # check that ocean O is around all edges of map

        self.first_row = self.lines[0]
        self.last_row = self.lines[self.geo_shape[0] - 1]
        self.first_column = [list(_)[0] for _ in self.lines]
        self.last_column = [list(_)[self.geo_shape[1] - 1]
                            for _ in self.lines]

        for letter in (self.first_row + self.last_row):
            if letter != 'O':
                raise ValueError("Ocean not on the edges")

        for letter in (self.first_column + self.last_column):
            if letter != 'O':
                raise ValueError("Ocean not on the edges")

        # Create Objects for each cell in the map

        dict_maps = {'O': Ocean, 'M': Mountain, 'J': Jungle, 'S': Savannah,
                     'D': Desert}
        self.object_matrix = []
        for row in range(self.geo_shape[0]):
            self.object_matrix.append([dict_maps[self.geo_list[row][column]](
                row, column) for column in range(self.geo_shape[1])])

    def get_plot(self):
        pass


if __name__ == "__main__":
    input_map = ("""\
                        OOOO
                        OJSO
                        OOOO""")
    g = Geo(input_map)
    print(g.object_matrix)

    x = [1,2,3]
    y = [2,4,6]
    sns.scatterplot(x,y)
    plt.show()
