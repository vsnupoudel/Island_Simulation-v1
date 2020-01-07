# -*- coding: utf-8 -*-

"""
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import numpy as np
import textwrap
import matplotlib.pyplot as plt


class GeographyArea:
    """
    Stores the size/shape of the geography, and the ID of each cell
    ID of cell can be S,J,D,O,F (Savanna, Jungle, Desert, Ocean, Fjell)
    """

    def __init__(self, geo_matrix_input_string):
        self.geo_graph = textwrap.dedent(geo_matrix_input_string)

    @property
    def geo_shape(self):
        return np.shape(self.geo_graph)


if __name__ == "__main__":
    g = GeographyArea("""\
    OOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOSMMMMJJJJJJJO
    OSSSSSJJJJMMJJJJJJJOO
    OSSSSSSSSSMMJJJJJJOOO
    OSSSSSJJJJJJJJJJJJOOO
    OSSSSSJJJDDJJJSJJJOOO
    OSSJJJJJDDDJJJSSSSOOO
    OOSSSSJJJDDJJJSOOOOOO
    OSSSJJJJJDDJJJJJJJOOO
    OSSSSJJJJDDJJJJOOOOOO
    OOSSSSJJJJJJJJOOOOOOO
    OOOSSSSJJJJJJJOOOOOOO
    OOOOOOOOOOOOOOOOOOOOO""")
    matrix = g.geo_graph
    print(type(matrix))
    b = matrix.splitlines()
    list_of_list= [ list(a) for a in b ]
    print(list_of_list)
    print(np.shape(list_of_list))
    print( list_of_list[0] [0])
    print( list_of_list[1] [8])



