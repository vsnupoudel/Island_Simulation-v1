# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo
import pytest


# class testGeo:
#     """ Tests for Geo class"""

def test_proper_letters():
    """all letters should either be: = O, M, J, S, D"""
    with pytest.raises(ValueError):
        Geo("yyyy")


def test_same_legth():
    """rows have same length"""
    with pytest.raises(ValueError):
        Geo(""""\
                OOOOOOO
                JJJJJ""")


def test_ocean_edges():
    with pytest.raises(ValueError):
        Geo(""""\
                OOOOO
                JJJJJ""")


def test_map_gives_object_output():
    g = Geo("""\
    OOO
    OJO
    OOO""")
    empty_list = []
    for row in g.object_matrix:
        empty_list.append([type(obj).__name__ for obj in row])
    assert empty_list == [['Ocean', 'Ocean', 'Ocean'],
                          ['Ocean', 'Jungle', 'Ocean'],
                          ['Ocean', 'Ocean', 'Ocean']]

def test_adjacent_cell():
    input_map = ("""\
                        OOOO
                        OJSO
                        OOOO""")
    g = Geo(input_map)
    # print(g.object_matrix)
    kun_migratable  = [type(cell).__name__ for cell in
                        g.get_adjacent_migratable_cells(1, 1)]
    all_four = [type(cell).__name__ for cell in
                g.get_adjacent_cells(1, 1)]

    assert kun_migratable == ['Savannah']
    assert all_four == ['Ocean', 'Ocean', 'Savannah', 'Ocean']



