# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from src.biosim.geography import CreateMap
import pytest


class TestGeo:
    """
    Several tests for the Geo class
    """
    @pytest.fixture()
    def create_map(self):
        """Creates a Geo object"""
        return CreateMap("""\
            OOO
            OJO
            OOO""")

    def test_map_gives_object_output(self, create_map):
        """create_map method should give cell objects as output"""
        empty_list = []
        for row in create_map.object_matrix:
            empty_list.append([type(obj).__name__ for obj in row])
        assert empty_list == [['Ocean', 'Ocean', 'Ocean'],
                              ['Ocean', 'Jungle', 'Ocean'],
                              ['Ocean', 'Ocean', 'Ocean']], \
            "Map not created properly"

    def test_proper_letters(self):
        """all letters should either be: = O, M, J, S, D"""
        with pytest.raises(ValueError):
            CreateMap("yyyy")

    def test_same_legth(self):
        """rows have same length"""
        with pytest.raises(ValueError):
            CreateMap(""""\
                    OOOOOOO
                    JJJJJ""")

    def test_ocean_edges(self):
        """There should only be ocean around the edges of the map"""
        with pytest.raises(ValueError):
            CreateMap(""""\
                    OOOOO
                    JJJJJ""")
