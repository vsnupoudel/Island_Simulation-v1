# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import numpy as np
import textwrap
import pandas as pd


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


        # check input characters
        for letter in self.geo_graph:
            if letter not in self.valid_list:

                raise ValueError

        self.lines = self.geo_graph.splitlines()
        self.geo_list = [ list(_) for _ in self.lines]

        #check equal length
        length_first = len(self.lines[0])
        for line in self.lines:
            if len(line) != length_first:
                raise ValueError

        #check O around edges of map

        first_row = self.lines[0]
        last_row = self.lines[self.geo_shape[0]]
        first_column = []
        last_column = []



    def geo_shape(self):
        """ Returns shape of the map"""

        return np.shape(self.geo_2D())

if __name__ == "__main__":
    g = Geo("""\
    OOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOSMMMMJJJJJJJO
    OSSSSSJJJJMMJJJJJJJOO""")





