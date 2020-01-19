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
    assert isinstance(G, Cell) & isinstance(M, Mountain)\
           & isinstance(J, Jungle) & isinstance(O, Ocean) & \
           isinstance(D, Desert) & isinstance(S,Savannah)

def test_positive_input_rows_columns():
    """all input sholud be positive integers"""
    jungle = Jungle(2,3)
    assert (jungle.row > 0) & (jungle.column > 0)

def test_positive_num_carn():
    """number of carnivores is a positive integer"""
    j = Jungle(2,3)
    assert (j.n_herbs >= 0) & (j.n_carns >= 0)

def test_set_and_get_function():
    j = Jungle(2, 3)
    # print(j.row, j.column, j.is_migratable)
    j.set_population({
            "loc": (2, 3),
            "pop": [{'species': 'Herbivore', 'age': 5, 'weight': 20},
                      {'species': 'Carnivore', 'age': 5, 'weight': 20}]})

    object_list = j.get_population()
    name_list = [type(a).__name__ for a in object_list]
    assert name_list == ["Herbivore","Carnivore"]

def test_sorted_herbs_and_carns():
    j = Jungle(2, 3)
    j.set_population({
            "loc": (2, 3),
            "pop": [{'species': 'Herbivore', 'age': 5, 'weight': 30},
                    {'species': 'Herbivore', 'age': 5, 'weight': 20},
                    {'species': 'Herbivore', 'age': 5, 'weight': 10}
                    ]})

    unsorted_fitness = [h.fitness for h in j.herb_list]
    sorted_fitness = sorted(unsorted_fitness)

    fitness_from_herb_sorted = [h.fitness for h in j.herb_sorted]

    assert fitness_from_herb_sorted == sorted_fitness
    assert [1,2] != [2,1]





