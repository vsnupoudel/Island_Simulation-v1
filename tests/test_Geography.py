# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from src.biosim.Geography import Geo
import pytest


class TestGeo:
    """
    Several tests for the Geo class
    """
    @pytest.fixture()
    def create_map(self):
        """Creates a Geo object"""
        return Geo("""\
            OOO
            OJO
            OOO""")

    def test_map_gives_object_output(self, create_map):

        empty_list = []
        for row in create_map.object_matrix:
            empty_list.append([type(obj).__name__ for obj in row])
        assert empty_list == [['Ocean', 'Ocean', 'Ocean'],
                              ['Ocean', 'Jungle', 'Ocean'],
                              ['Ocean', 'Ocean', 'Ocean']]

    def test_proper_letters(self):
        """all letters should either be: = O, M, J, S, D"""
        with pytest.raises(ValueError):
            Geo("yyyy")

    def test_same_legth(self):
        """rows have same length"""
        with pytest.raises(ValueError):
            Geo(""""\
                    OOOOOOO
                    JJJJJ""")

    def test_ocean_edges(self):
        with pytest.raises(ValueError):
            Geo(""""\
                    OOOOO
                    JJJJJ""")
