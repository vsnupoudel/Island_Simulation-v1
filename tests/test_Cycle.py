# -*- coding: utf-8 -*-

"""
Test for Cycle class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from Cycle import Cycle
from Geography import Geo
# from Mapping import Cell, Savannah, Jungle
from simulation import BioSim
import pytest
from pytest_mock import mocker


input_map = ("""\
                OOOO
                OJSO
                OOOO""")
ini_herbs = [
    {
        "loc": (1, 1),
        "pop": [
            {"species": "Herbivore", "age": 5, "weight": 50}
            for _ in range(120)
        ]
    }
]+[
    {
        "loc": (1, 1),
        "pop": [
            {"species": "Carnivore", "age": 5, "weight": 50}
            for _ in range(20)
        ]
    }
]

s = BioSim(input_map, ini_herbs, seed=1)
c = Cycle(s.object_matrix)

def test_get_adjacent_migratable_cells():
    """should only get migratable cells"""
    migratable_cells  = [type(cell).__name__ for cell in
                       c.get_adjacent_migratable_cells(1, 1)]
    assert migratable_cells == ['Savannah']

def test_food_grows_Savannah():
    """Food amount in each Savannah cell should increase"""
    prev_food_sav = c.object_matrix[1][2].f_ij
    c.food_grows()
    assert c.object_matrix[1][2].f_ij > prev_food_sav

def test_max_food_Jungle():
    """When food grows in Jungle cells it should be set to f_max = 800"""

    prev_food_jun = c.object_matrix[1][1].f_ij
    c.food_grows()
    assert c.object_matrix[1][1].f_ij >= prev_food_jun
    assert c.object_matrix[1][1].f_ij == c.object_matrix[1][1].parameters[
        'f_max']

def test_fitness_increase_after_feeding():
    prev_fitness_array = [ a.fitness for a in c.object_matrix[1][
        1].animal_object_list ]
    c.food_grows()
    c.animals_eat()
    curr_fitness_array = [a.fitness for a in c.object_matrix[1][
        1].animal_object_list]
    # cached property was not working in fitness, so removed it
    assert curr_fitness_array > prev_fitness_array

@pytest.fixture()
def h_count():
    return len([a for a in s.object_matrix[1][1].animal_object_list
    if type(a).__name__ == "Herbivore"] )

@pytest.fixture()
def c_count():
    return len([a for a in s.object_matrix[1][1].animal_object_list
                   if type(a).__name__ == "Carnivore"])


def test_animals_reproduce(h_count, c_count):
    herb_count_prev = h_count
    carn_count_prev = c_count

    c.food_grows()
    c.animals_reproduce()
    herb_count_curr = len([a for a in s.object_matrix[1][1].animal_object_list
    if type(a).__name__ == "Herbivore"])
    carn_count_curr = len([a for a in s.object_matrix[1][1].animal_object_list
                   if type(a).__name__ == "Carnivore"])

    assert carn_count_curr > carn_count_prev
    assert herb_count_curr > herb_count_prev

def test_animals_migrate(mocker):
    mocker.patch('numpy.random.random', return_value=0)
    c.animals_migrate()
    assert len(s.object_matrix[1][1].animal_object_list) == 0
    assert len(s.object_matrix[1][2].animal_object_list) == 140

def test_animals_dont_migrate(mocker):
    mocker.patch('numpy.random.random', return_value=1)
    c.animals_migrate()
    assert len(s.object_matrix[1][1].animal_object_list) == 140
    assert len(s.object_matrix[1][2].animal_object_list) == 0

def test_animals_migrate():
    c.animals_migrate()
    assert len(s.object_matrix[1][1].animal_object_list) > 0
    assert len(s.object_matrix[1][1].animal_object_list) < 140
    assert len(s.object_matrix[1][2].animal_object_list) > 0
    assert len(s.object_matrix[1][2].animal_object_list) < 140

def test_all_animals_die(mocker):
    mocker.patch('numpy.random.random', return_value=0)
    c.animals_die()
    assert s.object_matrix[1][1].animal_object_list == []

def test_no_animals_die(mocker):
    mocker.patch('numpy.random.random', return_value=1)
    old_list = s.object_matrix[1][1].animal_object_list
    c.animals_die()
    assert s.object_matrix[1][1].animal_object_list == old_list

def test_animals_die(mocker):
    mocker.patch('numpy.random.random', return_value=0.001)
    old_len = len(s.object_matrix[1][1].animal_object_list)
    c.animals_die()
    assert len(s.object_matrix[1][1].animal_object_list) < old_len


