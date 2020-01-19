# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from src.biosim.Mapping import Savannah, Jungle, Desert, Ocean, Mountain, Cell

def test_is_instance():
    G = Cell(2, 3)
    M= Mountain(2,3)
    J= Jungle(2,3)
    O = Ocean(2,3)
    D = Desert(2,3)
    S = Savannah(2,3)
    assert isinstance(G, Cell) & isinstance(M, Mountain) & isinstance(J, Jungle) \
           & isinstance(O, Ocean) & isinstance(D, Desert) & isinstance(S,Savannah)

def test_positive_input_rows_columns():
    """all input sholud be positive integers"""
    jungle = Jungle(2,3)
    assert (jungle.row > 0) & (jungle.column > 0)

def test_positive_num_carn():
    """number of carnevoirs is a positive integer"""
    j = Jungle(2,3)
    assert (j.num_carnivores >= 0) & (j.num_herb >= 0)

def test_set_and_get_function():
    j = Jungle(2, 3)
    # print(j.row, j.column, j.is_migratable)
    j.set_population([{'species': 'Herbivore', 'age': 5, 'weight': 20}, \
                      {'species': 'Herbivore', 'age': 5, 'weight': 20}])
    assert j.get_population()==[{'species': 'Herbivore', 'age': 5, 'weight': 20}, \
                      {'species': 'Herbivore', 'age': 5, 'weight': 20}]


