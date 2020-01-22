# -*- coding: utf-8 -*-

"""
CreateMap class
"""

__author__ = "Anders Huse; Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import numpy as np
import textwrap
from terrain import Jungle, Savannah, Desert, Ocean, Mountain


class CreateMap:
    """
    Class for the islands geography. This class:

    - Stores the size/shape of the geography of the island
    - Converts string input of map, consisting of letters corresponding to
      landscape types into a 2D matrix of objects
    - Objects can only be one of the five Landscape types: Ocean (O), Savannah
      (S), desert (D), jungle (J) and mountain (M)

    :ivar geo_matrix_input_string:    str, String with map coordinates
    :ivar geo_graph:                  str, input string without whitespace
    :ivar lines:                     list, list of each line of the input
                                     string
    :ivar geo_shape:                 tuple(default, None), Shape of the
                                     geography
    :ivar object_matrix:             list, 2D list of cell objects
    :ivar geo_list:                  list, 2D list of string characters
    :ivar first_row:                 str, characters of the first row of the
                                     map
    :ivar last_row:                  str, characters of the last row of the map
    :ivar first_column:              list, characters of the first column of
                                     the map
    :ivar last_column:               list, characters of the last column of
                                     the map

    """
    valid_landscape_list = ['O', 'S', 'D', 'J', 'M']

    def __init__(self, geo_matrix_input_string):
        """
        - Checks if input characters are valid letters
        - Checks if all rows in map have equal length
        - Checks that ocean ("O") is around all edges of map

        :param geo_matrix_input_string:   str, String with map coordinates
        """
        self.geo_graph = textwrap.dedent(geo_matrix_input_string)
        self.lines = self.geo_graph.splitlines()
        self.geo_shape = None
        self.object_matrix = []

        # check if input characters are valid letters
        for line in self.lines:
            for letter in line:
                if letter not in self.valid_landscape_list:
                    raise ValueError(" Invalid Letters in the Input map ")

        self.geo_list = [list(_) for _ in self.lines]  # each letter separated
        self.geo_shape = np.shape(self.geo_list)

        # Check if all rows in map have equal length
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

        # Change the letters in Map to corresponding Objects
        dict_maps = {'O': Ocean, 'M': Mountain, 'J': Jungle, 'S': Savannah,
                     'D': Desert}
        for row_num in range(self.geo_shape[0]):
            self.object_matrix.append(
                [dict_maps[self.geo_list[row_num][column]](row_num, column)
                 for column in range(self.geo_shape[1])])
