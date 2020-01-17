# -*- coding: utf-8 -*-

"""
Tests for Animal class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.simulation import BioSim
from biosim.Mapping import Cell, Savannah, Jungle
from biosim.Animal import Herbivore, Carnivore

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

ini_carns = [
        {
            "loc": (2, 2),
            "pop": [
                {"species": "Carnivore", "age": 5, "weight": 20}
                for _ in range(40)
            ],
        }
    ]

s = BioSim(map, ini_herbs, seed=1)

def test_current_year():
    """Tests correctness of current_year propertie"""

    assert s.current_year >= 0


def test_set_landscape_parameters():
    "set_landscape_parameters shold change parameters sucsessfully"

    s.set_landscape_parameters("S", {"f_max": 700})
    s.set_landscape_parameters("J", {"f_max": 600})

    assert Savannah.parameters["f_max"] == 700
    assert Jungle.parameters["f_max"] == 600



def test_set_animal_parameters():
    "set_animal_parameters shold change parameters sucsessfully"

    s.set_animal_parameters("Herbivore", {"zeta": 3.2, "xi": 1.8})
    s.set_animal_parameters("Carnivore", {"zeta": 5.0, "xi": 2.0})

    assert Herbivore.p["zeta"] == 3.2
    assert Herbivore.p["xi"] == 1.8
    assert Carnivore.p["zeta"] == 5.0
    assert Carnivore.p["xi"] == 2.0


def test_num_animals():
    """"""
    assert s.num_animals['Herbivore'] >= 0
    assert s.num_animals['Carnivore'] >= 0


def test_add_population():
    """"""
    #pop before
    s.add_population(ini_carns)
    #pop after
    #assert pop_after > pop_before
    pass


def test_shape_herbivore_distributin():
    """shape of herbivore_distribution should be the same as for
    the object_matrix"""
    np.shape(s.herbivore_distribution.shape) == np.shape(s.object_matrix)
    pass


def test_shape_carnivore_distributin():
    """shape of carnivore_distribution should be the same as for
     the object_matrix"""
    np.shape(s.carnivore_distribution.shape) == np.shape(s.object_matrix)
    pass


def test_carnivore_distributin():
    """test for carnivore_distribution property"""
    s.carnivore_distribution
    pass


def test_animal_distributin():
    """test for animal_distribution property"""
    s.animal_distribution
    pass


def test_island_matrix_shape():
    """test island_matrix property"""
    assert np.shape(s.island_matrix) == np.shape(s.object_matrix)


def test_island_matrix():
    """test island_matrix property"""
    pass


def test_simulation():
    """test for simulation method"""
    pass




