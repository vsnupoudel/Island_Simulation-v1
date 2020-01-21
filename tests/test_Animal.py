# -*- coding: utf-8 -*-

"""
Tests for Animal class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from animal import Animal, Herbivore, Carnivore
from geography import Geo
from cycle import Cycle
from mapping import Cell, Jungle

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

    @pytest.fixture()
    def herb_zeta_3(self, create_herb):
        """sets zeta parameter of herbivores to 3"""
        create_herb.up_par({"zeta": 3.0})
        yield create_herb.p["zeta"]
        create_herb.up_par({"zeta": 3.5})

    def test_update_zeta_herbs(self, create_herb, herb_zeta_3):
        """zeta parameter of herbivores should be updated to 3.0"""
        assert herb_zeta_3 == 3.0,  "parameter not updated sucsessfully"

    @pytest.fixture()
    def carn_xi_2(self, create_carn):
        """sets xi parameter of carnivores to 2"""
        create_carn.up_par({"xi": 2.0})
        yield create_carn.p["xi"]
        create_carn.up_par({"xi": 3.5})

    def test_update_xi_carns(self, create_carn, carn_xi_2):
        """xi parameter of carnivores should be updated to 2.0"""
        assert carn_xi_2 == 2.0, "parameter not updated sucsessfully"

    def test_animal_not_dead(self, create_herb, create_carn):
        """ New animal should not be dead"""

        assert create_herb.is_dead is False, "Animal should not be dead"
        assert create_carn.is_dead is False, "Animal should not be dead"

    def test_positive_input(self, create_herb, create_carn):
        """age and weight should be positive"""

        assert create_herb.age > 0 and (create_herb.weight > 0), \
            "parameter should be positive"

        assert create_carn.age > 0 and (create_carn.weight > 0), \
            "parameter should be positive"

    def test_positive_fitness(self, create_herb, create_carn):
        """Animal should have positive fitness"""

        assert create_herb.fitness > 0, "Fitness should be positive"
        assert create_carn.fitness > 0, "Fitness should be positive"

    def test_herb_eat_weight_increase(self, create_herb, create_cycle):
        """Herbivores weight should increase when eating"""
        prev_weigth = create_herb.weight
        create_herb.herb_eat(create_cycle.object_matrix[1][2])

        assert create_herb.weight > prev_weigth,  \
             "Herbivores weigth should increase after eating"

    def test_herb_eat_weight_increase_right_amount(self, create_herb,
                                                   create_cycle):
        """Herbivores weight should increase with (p['beta'] * p['F'])
        when eating and food avilable is more than appetite"""
        prev_weight = create_herb.weight
        create_herb.herb_eat(create_cycle.object_matrix[1][1])

        assert create_herb.weight - prev_weight == \
               create_herb.p['beta'] * create_herb.p['F'],  \
             "Herbivores weigth increase with wrong amount"

    def test_animal_reproduce_weight_decrease(self, mocker):
        """Animals weight should decrease when giving birth"""
        h = Herbivore(2, 50)
        c = Carnivore(2, 50)
        prev_weight_h = h.weight
        prev_weight_c = c.weight
        mocker.patch('numpy.random.random', return_value=0)
        h.herb_reproduce(10)
        c.carn_reproduce(10)

        assert h.weight < prev_weight_h, \
            "Weight should decrease after reproduction"
        assert c.weight < prev_weight_c, \
            "Weight should decrease after reproduction"

    def test_animal_reproduce_baby_age_zero(self, mocker):
        """Age of newborn animal should be zero"""
        h = Herbivore(2, 50)
        c = Carnivore(2, 50)
        mocker.patch('numpy.random.random', return_value=0)
        new_herb = h.herb_reproduce(10)
        new_carn = c.carn_reproduce(10)

        assert new_herb.age == 0, "Newborn age should be zero"
        assert new_carn.age == 0, "Newborn age should be zero"

    def test_animal_reproduce_baby_weigth_positive(self, mocker):
        """Weigth of newborn animal should be positive"""
        h = Herbivore(2, 50)
        c = Carnivore(2, 50)
        mocker.patch('numpy.random.random', return_value=0)
        new_herb = h.herb_reproduce(10)
        new_carn = c.carn_reproduce(10)

        assert new_herb.weight > 0, "Newborn weigth should be positive"
        assert new_carn.weight > 0, "Newborn weigth should be positive"

    def test_animals_migrate_adjacent_cell(self, mocker):
        """Animals migrate to a adjacent cell"""
        h = Herbivore(5, 10)
        c = Carnivore(5, 10)
        cell_1 = Cell(1, 2)
        cell_2 = Cell(0, 1)
        # mocker.patch('numpy.random.random', return_value=0)
        h.herb_migrates(h, (1, 1), [cell_1], [1])
        c.carn_migrates(c, (0, 0), [cell_2], [1])

        assert len(cell_1.animal_object_list) == 1, "Migration unsucsessfull"
        assert len(cell_2.animal_object_list) == 1, "Migration unsucsessfull"

