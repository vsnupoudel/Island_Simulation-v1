# -*- coding: utf-8 -*-

"""
Test for Cycle class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from Cycle import Cycle
from simulation import BioSim
from pytest_mock import mocker
import pytest
import numpy


@pytest.fixture()
def input_map():
    map = ("""\
                    OOOO
                    OJSO
                    OOOO""")
    return map


@pytest.fixture()
def ini_herbs():
    herbs = [
                    {
                        "loc": (1, 1),
                        "pop": [
                            {"species": "Herbivore", "age": 5, "weight": 50}
                            for _ in range(120)
                        ]
                    }
                ] + [
                    {
                        "loc": (1, 1),
                        "pop": [
                            {"species": "Carnivore", "age": 5, "weight": 50}
                            for _ in range(20)
                        ]
                    }
                ]
    return herbs


@pytest.fixture()
def create_s(input_map,ini_herbs):
    s = BioSim(input_map, ini_herbs, seed=1)
    return s


@pytest.fixture()
def create_c(input_map,ini_herbs, create_s):
    c = Cycle(create_s.object_matrix)
    return c


def test_get_adjacent_migratable_cells(create_c):
    """should only get migratable cells"""
    migratable_cells  = [type(cell).__name__ for cell in
                       create_c.get_adjacent_migratable_cells(1, 1)]
    assert migratable_cells == ['Savannah']


def test_food_grows_Savannah(create_c):
    """Food amount in each Savannah cell should increase"""
    prev_food_sav = create_c.object_matrix[1][2].f_ij
    create_c.food_grows()
    assert create_c.object_matrix[1][2].f_ij > prev_food_sav


def test_max_food_Jungle(create_c):
    """When food grows in Jungle cells it should be set to f_max = 800"""

    prev_food_jun = create_c.object_matrix[1][1].f_ij
    create_c.food_grows()
    assert create_c.object_matrix[1][1].f_ij >= prev_food_jun
    assert create_c.object_matrix[1][1].f_ij == create_c.object_matrix[1][1].parameters[
        'f_max']


def test_fitness_increase_after_feeding(create_c):
    prev_fitness_array = [ a.fitness for a in create_c.object_matrix[1][
        1].animal_object_list ]
    create_c.food_grows()
    create_c.animals_eat()
    curr_fitness_array = [a.fitness for a in create_c.object_matrix[1][
        1].animal_object_list]
    # cached property was not working in fitness, so removed it
    assert curr_fitness_array > prev_fitness_array


def test_animals_reproduce(input_map, ini_herbs):
    s = BioSim(input_map, ini_herbs, seed=1)
    herb_count_prev = s.object_matrix[1][1].n_herbs
    carn_count_prev = s.object_matrix[1][1].n_carns

    c = Cycle(s.object_matrix)
    c.food_grows()
    c.animals_reproduce()
    herb_count_curr = s.object_matrix[1][1].n_herbs
    carn_count_curr = s.object_matrix[1][1].n_carns

    assert carn_count_curr > carn_count_prev
    assert herb_count_curr > herb_count_prev


def test_animals_migrate(mocker, create_c, create_s):
    mocker.patch('numpy.random.random', return_value=0)
    create_c.animals_migrate()
    assert len(create_s.object_matrix[1][1].animal_object_list) == 0
    assert len(create_s.object_matrix[1][2].animal_object_list) == 140


def test_animals_dont_migrate(mocker,create_c, create_s):
    mocker.patch('numpy.random.random', return_value=1)
    create_c.animals_migrate()
    assert len(create_s.object_matrix[1][1].animal_object_list) == 140
    assert len(create_s.object_matrix[1][2].animal_object_list) == 0


def test_animals_migrate(create_c, create_s):
    create_c.animals_migrate()
    assert len(create_s.object_matrix[1][1].animal_object_list) > 0
    assert len(create_s.object_matrix[1][1].animal_object_list) < 140
    assert len(create_s.object_matrix[1][2].animal_object_list) > 0
    assert len(create_s.object_matrix[1][2].animal_object_list) < 140


def test_all_animals_die(mocker, create_c, create_s ):
    mocker.patch('numpy.random.random', return_value=0)
    create_c.animals_die()
    assert create_s.object_matrix[1][1].animal_object_list == []


def test_no_animals_die(mocker, create_c, create_s):
    mocker.patch('numpy.random.random', return_value=1)
    old_list = create_s.object_matrix[1][1].animal_object_list
    create_c.animals_die()
    assert create_s.object_matrix[1][1].animal_object_list == old_list


def test_death_probability(mocker, create_c, create_s):
    mocker.patch('numpy.random.random', return_value=0.001)
    obj_id = id( create_s.object_matrix[1][1].animal_object_list[0] )
    death_prob = create_s.object_matrix[1][1].animal_object_list[0].death_prob
    create_c.animals_die()
    list_id = [id(a) for a in create_s.object_matrix[1][1].animal_object_list]
    if numpy.random.random() < death_prob:
        assert obj_id not in list_id
    else:
        assert obj_id in list_id