# -*- coding: utf-8 -*-

"""
"""

__author__ = ""
__email__ = ""

import numpy as np
import textwrap


class Geo:
    """
    Stores the size/shape of the geography, and the ID of each cell
    ID of cell can be S,J,D,O,F (Savanna, Jungle, Desert, Ocean, Fjell)
    """

    def __init__(self, geo_matrix_input_string):
        self.geo_graph = textwrap.dedent(geo_matrix_input_string)

    def geo_graph(self):
        """
        Makes a 2D list of the coordinates for the geography
        """
        lines = self.geo_graph_string.splitline()
        geo_list = [ list(_) for _ in lines]
        return geo_list

    @property
    def geo_shape(self):
        return np.shape(self.geo_graph)


