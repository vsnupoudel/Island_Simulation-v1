# -*- coding: utf-8 -*-

"""
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import numpy as np
import textwrap


class Geo:
    """
    Stores the size/shape of the geography, and the ID of each cell
    ID of cell can be S,J,D,O,F (Savanna, Jungle, Desert, Ocean, Fjell)
    """

    def __init__(self, geo_matrix_input_string):
        self.geo_graph = textwrap.dedent(geo_matrix_input_string)

    def geo_2D(self):
        """
        Makes a 2D list of the coordinates for the geography
        """
        lines = self.geo_graph.splitline()
        geo_list = [ list(_) for _ in lines]
        return geo_list

    @property
    def geo_shape(self):
        return np.shape(self.geo_graph)


if __name__ == "__main__":
    g = Geo("""\
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

    a = g.geo_2D()
    print(a)



