# -*- coding: utf-8 -*-

"""
Tests for Animal class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from simulation import BioSim
from Mapping import Savannah, Jungle
from Animal import Herbivore, Carnivore
import numpy as np
import pytest
from pytest_mock import mocker


@pytest.fixture()
def input_map():
    """returns map where required in tests below"""
    map = """\
                 OOOOOOOOO
                 OSSJJSSOO
                 OOOOOOOOO
                 """
    return map

@pytest.fixture()
def ini_herbs():
    """returns herbivore population where required in tests below"""
    herbs = [
        {
            "loc": (2, 2),
            "pop": [
                {"species": "Herbivore", "age": 5, "weight": 20}
                for _ in range(200)
            ]+[
                {"species": "Carnivore", "age": 5, "weight": 20}
                for _ in range(200)
            ]
        },
        {
            "loc": (2, 3),
            "pop": [
                {"species": "Herbivore", "age": 5, "weight": 20}
                for _ in range(200)
            ]
        }
    ]
    return herbs

@pytest.fixture()
def ini_carns():
    carns = [
            {
                "loc": (2, 2),
                "pop": [
                    {"species": "Carnivore", "age": 5, "weight": 20}
                    for _ in range(40)
                ]
            }
        ]
    return carns

@pytest.fixture()
def create_s(input_map, ini_herbs):
    s = BioSim(input_map, ini_herbs, seed=1)
    return s


def test_set_landscape_parameters(create_s):
    "set_landscape_parameters shold change parameters sucsessfully"

    create_s.set_landscape_parameters("S", {"f_max": 700})
    create_s.set_landscape_parameters("J", {"f_max": 600})
    assert Savannah.parameters["f_max"] == 700
    assert Jungle.parameters["f_max"] == 600


def test_set_animal_parameters(create_s):
    "set_animal_parameters shold change parameters sucsessfully"

    create_s.set_animal_parameters("Herbivore", {"zeta": 3.2, "xi": 1.8})
    create_s.set_animal_parameters("Carnivore", {"zeta": 5.0, "xi": 2.0})

    assert Herbivore.p["zeta"] == 3.2
    assert Herbivore.p["xi"] == 1.8
    assert Carnivore.p["zeta"] == 5.0
    assert Carnivore.p["xi"] == 2.0


def test_num_animals(input_map, ini_herbs):
    """"""
    s = BioSim(input_map, ini_carns, seed=1)
    print('')
    print(s.num_animals['Herbivore'])
    print(s.num_animals['Carnivore'])
    assert s.num_animals['Herbivore'] > 0
    # assert s.num_animals['Carnivore'] > 0
    # s.add_population(ini_carns)
    # assert create_s.num_animals['Carnivore'] > 0


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


class TestSimulation:
    """
    Several tests for the Simulation class
    """

    @pytest.fixture()
    def input_map(self):
        """returns map where required in tests below"""
        map = """\
                     OOOOOOOOO
                     OSSJJSSOO
                     OOOOOOOOO
                     """
        return map

    @pytest.fixture()
    def ini_herbs(self):
        """returns herbivore population where required in tests below"""
        herbs = [
            {
                "loc": (2, 2),
                "pop": [
                           {"species": "Herbivore", "age": 5, "weight": 20}
                           for _ in range(200)
                       ] + [
                           {"species": "Carnivore", "age": 5, "weight": 20}
                           for _ in range(200)
                       ]
            },
            {
                "loc": (2, 3),
                "pop": [
                    {"species": "Herbivore", "age": 5, "weight": 20}
                    for _ in range(200)
                ]
            }
        ]
        return herbs

    @pytest.fixture()
    def ini_carns(self):
        carns = [
            {
                "loc": (2, 2),
                "pop": [
                    {"species": "Carnivore", "age": 5, "weight": 20}
                    for _ in range(40)
                ]
            }
        ]
        return carns

    @pytest.fixture()
    def create_s(self,input_map, ini_herbs):
        s = BioSim(input_map, ini_herbs, seed=1)
        return s

    def test_set_landscape_parameters(self, create_s):
        "set_landscape_parameters shold change parameters sucsessfully"

        create_s.set_landscape_parameters("S", {"f_max": 700})
        create_s.set_landscape_parameters("J", {"f_max": 600})

        assert Savannah.parameters["f_max"] == 700
        assert Jungle.parameters["f_max"] == 600

    def test_set_animal_parameters(self, create_s):
        "set_animal_parameters shold change parameters sucsessfully"

        create_s.set_animal_parameters("Herbivore", {"zeta": 3.2, "xi": 1.8})
        create_s.set_animal_parameters("Carnivore", {"zeta": 5.0, "xi": 2.0})

        assert Herbivore.p["zeta"] == 3.2
        assert Herbivore.p["xi"] == 1.8
        assert Carnivore.p["zeta"] == 5.0
        assert Carnivore.p["xi"] == 2.0

    def test_num_animals(self, input_map, ini_herbs):
        """"""
        s = BioSim(input_map, ini_carns, seed=1)
        print('')
        print(s.num_animals['Herbivore'])
        print(s.num_animals['Carnivore'])
        assert s.num_animals['Herbivore'] > 0
        # assert s.num_animals['Carnivore'] > 0
        # s.add_population(ini_carns)
        # assert create_s.num_animals['Carnivore'] > 0

    def test_add_population(self):
        """"""
        # pop before
        s.add_population(ini_carns)
        # pop after
        # assert pop_after > pop_before
        pass

    def test_shape_herbivore_distributin(self):
        """shape of herbivore_distribution should be the same as for
        the object_matrix"""
        np.shape(s.herbivore_distribution.shape) == np.shape(s.object_matrix)
        pass

    def test_shape_carnivore_distributin(self):
        """shape of carnivore_distribution should be the same as for
         the object_matrix"""
        np.shape(s.carnivore_distribution.shape) == np.shape(s.object_matrix)
        pass

    def test_carnivore_distributin(self):
        """test for carnivore_distribution property"""
        s.carnivore_distribution
        pass

    def test_animal_distributin(self):
        """test for animal_distribution property"""
        s.animal_distribution
        pass

    def test_island_matrix_shape(self):
        """test island_matrix property"""
        assert np.shape(s.island_matrix) == np.shape(s.object_matrix)

    def test_island_matrix(self):
        """test island_matrix property"""
        pass

    def test_simulation(self):
        """test for simulation method"""
        pass
