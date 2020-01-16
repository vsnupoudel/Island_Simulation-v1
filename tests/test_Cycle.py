# -*- coding: utf-8 -*-

"""
Test for Cycle class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Cycle import Cycle
from biosim.Geography import Geo

def test_get_adjacent_migratable_cells():
    input_map = ("""\
                        OOOO
                        OJSO
                        OOOO""")
    g = Geo(input_map)
    c = Cycle(g.object_matrix)
    # print(g.object_matrix)
    kun_migratable  = [type(cell).__name__ for cell in
                        c.get_adjacent_migratable_cells(1, 1)]

    assert kun_migratable == ['Savannah']