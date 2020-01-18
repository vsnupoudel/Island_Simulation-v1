# -*- coding: utf-8 -*-

"""
Tests for Animal class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from Animal import Animal, Herbivore, Carnivore
from Geography import Geo
from Cycle import Cycle
from Mapping import Cell

import pytest
import pytest_mock
import numpy as np
import random


class TestAnimal:
    """
    Several tests for the animal class
    """

    @pytest.fixture()
    def create_herb(self):
        """Creates a Herbivore object"""
        herb = Herbivore(5, 10)
        return herb

    @pytest.fixture()
    def create_carn(self):
        """Creates a Carnivore object"""
        carn = Carnivore(5, 10)
        return carn

    @pytest.fixture()
    def create_geo(self):
        """Creates a Geo object"""
        input_map = ("""\
                                OOOO
                                OJSO
                                OOOO""")
        return Geo(input_map)

    @pytest.fixture()
    def create_cycle(self, create_geo):
        """Creates a Cycle object"""
        return Cycle(create_geo.object_matrix)


    def test_animal_not_dead(self, create_herb, create_carn):
        """ New animal should not be dead"""

        assert create_herb.is_dead is False
        assert create_carn.is_dead is False

    def test_positive_input(self, create_herb, create_carn):
        """age and weight should be positive"""

        assert create_herb.age > 0 and (create_herb.weight > 0)
        assert create_carn.age > 0 and (create_carn.weight > 0)

    def test_positive_fitness(self, create_herb, create_carn):
        """Animal should have positive fitness"""

        assert create_herb.fitness > 0
        assert create_carn.fitness > 0

    def test_up_par(self, create_herb, create_carn):
        """Herbivore and Carnivore parameters should be updated"""

        create_herb.up_par({"zeta": 3.2, "xi": 1.8})
        create_carn.up_par({"zeta": 5.0, "xi": 2.0})

        assert create_herb.p["zeta"] == 3.2
        assert create_herb.p["xi"] == 1.8
        assert create_carn.p["zeta"] == 5.0
        assert create_carn.p["xi"] == 2.0

    def test_herb_eat_weight_increase(self, create_herb, create_cycle):
        """Herbivores weight should increase when eating"""
        prev_weigth = create_herb.weight
        create_herb.herb_eat(create_cycle.object_matrix[1][2])

        assert create_herb.weight > prev_weigth

    def test_animal_reproduce_weight_decrease(self, mocker):
        """Animals weight should decrease when giving birth"""
        h = Herbivore(2, 50)
        c = Carnivore(2, 50)
        prev_weight_h = h.weight
        prev_weight_c = c.weight
        mocker.patch('numpy.random.random', return_value=0)
        h.herb_reproduce(10)
        c.carn_reproduce(10)

        assert np.random.random() == 0

        assert h.weight < prev_weight_h
        assert c.weight < prev_weight_c

    def test_animal_reproduce_baby_age_zero(self, mocker):
        """Age of newborn animal should be zero"""
        h = Herbivore(2, 50)
        c = Carnivore(2, 50)
        mocker.patch('numpy.random.random', return_value=0)
        new_herb = h.herb_reproduce(10)
        new_carn = c.carn_reproduce(10)

        assert new_herb.age == 0
        assert new_carn.age == 0

    def test_animal_reproduce_baby_weigth_positive(self, mocker):
        """Weigth of newborn animal should be positive"""
        h = Herbivore(2, 50)
        c = Carnivore(2, 50)
        mocker.patch('numpy.random.random', return_value=0)
        new_herb = h.herb_reproduce(10)
        new_carn = c.carn_reproduce(10)

        assert new_herb.weight > 0
        assert new_carn.weight > 0

    def test_animals_migrate_adjacent_cell(self, mocker):
        """Animals migrate to a adjacent cell"""
        h = Herbivore(5, 10)
        c = Carnivore(5, 10)
        cell_1 = Cell(1, 2)
        cell_2 = Cell(0, 1)
        mocker.patch('numpy.random.random', return_value=0)
        h.herb_migrates(h, (1, 1), [cell_1], [1])
        c.carn_migrates(c, (0, 0), [cell_2], [1])

        assert len(cell_1.animal_object_list) == 1
        assert len(cell_2.animal_object_list) == 1

















