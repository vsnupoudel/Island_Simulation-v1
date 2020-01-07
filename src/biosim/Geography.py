# -*- coding: utf-8 -*-

"""
"""

__author__ = ""
__email__ = ""


class Geo:
    """
    Stores the size/shape of the geography, and the ID of each cell
    ID of cell can be S,J,D,O,F (Savanna, Jungle, Desert, Ocean, Fjell)
    """

    def __init__(self, geo_matrix_input_string):
        self.geo_graph = textwrap.dedent(geo_matrix_input_string)

    @property
    def geo_shape(self):
        return np.shape(self.geo_graph)
        

