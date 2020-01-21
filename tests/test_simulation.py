# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.simulation import BioSim
from biosim.mapping import Savannah, Jungle
from biosim.animal import Herbivore, Carnivore
import numpy as np
import pytest


class TestSimulation:
    """Tests for the Biosim class"""

    @pytest.fixture()
    def input_map(self):
        """returns map where required in tests below"""

        return """\
                     OOOOOOOOO
                     OSSJJSSOO
                     OOOOOOOOO
                     """

    @pytest.fixture()
    def ini_pop(self):
        """returns herbivore population where required in tests below"""
        herbs = [
            {
                "loc": (1, 2),
                "pop": [
                    {"species": "Herbivore", "age": 5, "weight": 20}
                    for _ in range(200)
                ]+[
                    {"species": "Carnivore", "age": 5, "weight": 20}
                    for _ in range(200)
                ]
            },
            {
                "loc": (1, 3),
                "pop": [
                    {"species": "Herbivore", "age": 5, "weight": 20}
                    for _ in range(200)
                ]
            }
        ]
        return herbs

    @pytest.fixture()
    def add_carns(self):
        """
        Returns carnivore population where required in tests below
        Population should be an iterable
        """
        carns = [
            {
                "loc": (2, 2),
                "pop": [
                    {"species": "Carnivore", "age": 5, "weight": 20}
                    for _ in range(40)
                ],
            }
        ]
        return carns

    @pytest.fixture()
    def create_s(self, input_map, ini_pop):
        """Makes BioSim object"""
        return BioSim(input_map, ini_pop, seed=1)

    def test_set_landscape_parameters(self, create_s):
        """set_landscape_parameters shold change parameters sucsessfully"""
        create_s.set_landscape_parameters("S", {"f_max": 700})
        create_s.set_landscape_parameters("J", {"f_max": 600})
        assert Savannah.parameters["f_max"] == 700
        assert Jungle.parameters["f_max"] == 600

    def test_set_animal_parameters(self, create_s):
        """set_animal_parameters shold change parameters sucsessfully"""

        create_s.set_animal_parameters("Herbivore", {"zeta": 3.2, "xi": 1.8})
        create_s.set_animal_parameters("Carnivore", {"zeta": 5.0, "xi": 2.0})
        assert Herbivore.animal_params["zeta"] == 3.2
        assert Herbivore.animal_params["xi"] == 1.8
        assert Carnivore.animal_params["zeta"] == 5.0
        assert Carnivore.animal_params["xi"] == 2.0

    def test_num_animals_and_add_population(self, input_map, ini_pop,
                                            add_carns):
        """"""
        s = BioSim(input_map, ini_pop, seed=1)
        assert s.num_animals_per_species['Herbivore'] > 0
        assert s.num_animals_per_species['Carnivore'] > 0
        prev_carns = s.num_animals_per_species['Carnivore']
        s.add_population(add_carns)
        assert s.num_animals_per_species['Carnivore'] > prev_carns

    def test_shape_herbivore_distributin(self, create_s):
        """shape of herbivore_distribution should be the same as for
        the object_matrix"""
        assert np.shape(create_s.herbivore_distribution) ==\
            np.shape(create_s.object_matrix)

    def test_shape_carnivore_distributin(self, create_s):
        """shape of carnivore_distribution should be the same as for
         the object_matrix"""
        assert np.shape(create_s.carnivore_distribution) ==\
            np.shape(create_s.object_matrix)

    def test_carnivore_distributin(self, create_s):
        """test for carnivore_distribution property"""
        assert 200 in create_s.carnivore_distribution

    def test_island_matrix_shape(self, create_s):
        """test island_matrix property"""
        assert np.shape(create_s.island_matrix) == np.shape(
            create_s.object_matrix)

    def test_simulate_function(self, input_map, ini_pop):
        s = BioSim(input_map, ini_pop, seed=123)
        prev_number_of_animals = s.num_animals_per_species
        s.simulate()
        assert s.num_animals_per_species['Herbivore'] !=\
            prev_number_of_animals['Herbivore']
        assert s.num_animals_per_species['Carnivore'] !=\
            prev_number_of_animals['Carnivore']

    def test_make_movie(self, create_s):
        pass
