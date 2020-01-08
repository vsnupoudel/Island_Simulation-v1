# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import numpy as np
import textwrap
import pandas as pd
from biosim.Mapping import  Jungle  ,Savannah, Desert, Ocean, Mountain


class Geo:
    """
    Stores the size/shape of the geography, and the ID of each cell
    ID of cell can be S,J,D,O,F (Savanna, Jungle, Desert, Ocean, Fjell)
    """
    valid_list = ['O', 'S', 'D', 'J', 'M']

    def __init__(self, geo_matrix_input_string):
        """
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
        self.last_column = [list(_)[self.geo_shape[1] - 1] \
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
        self.geo_ob_array = []
        for row in range(self.geo_shape[0]):
            self.geo_ob_array.append([dict_maps[self.geo_list[row][column]]( \
                row, column) for column in range(self.geo_shape[1])])


if __name__ == "__main__":
    g = Geo("""\
    OOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOJMMMMJJJJJJJO
    OSSSSSJJJJJJJJJJJJJOO
    OOOOOOOOOOOOOOOOOOOOO""")
    for row in g.geo_ob_array:
        arr= [ type(obj).__name__  for obj in row]
        print(arr)
