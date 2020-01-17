# -*- coding: utf-8 -*-

"""
Tests for Animal class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"


from biosim.simulation import BioSim
from biosim.Mapping import Cell, Savannah, Jungle
from biosim.Animal import Herbivore, Carnivore
from biosim.Visualization import Visualization

import numpy as np

map = """\
             OOOOOOOOO
             OSSJJSSOO
             OOOOOOOOO
             """

ini_herbs = [
    {
        "loc": (2, 2),
        "pop": [
            {"species": "Herbivore", "age": 5, "weight": 20}
            for _ in range(200)
        ],
    }
]

s = BioSim(map, ini_herbs, seed=1)
v = Visualization(s.object_matrix)


def test_set_graphics():
    """tests subplots of set_graphics"""
    v._set_graphics()
    assert v._fig is not None
    assert v._map_ax is not None
    assert v._herb_line is not None
    assert v._carn_line is not None
    assert v._herb_ax is not None
    assert v._carn_ax is not None


def test_create_map():
    """Map should be created"""
    v.create_map(s.carnivore_distribution)
    assert v._img_axis is not None




