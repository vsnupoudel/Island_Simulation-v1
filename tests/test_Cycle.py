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

input_map = ("""\
                OOOO
                OJSO
                OOOO""")
ini_herbs = [
    {
        "loc": (10, 10),
        "pop": [
            {"species": "Herbivore", "age": 5, "weight": 20}
            for _ in range(150)
        ],
    }
]

s = BioSim(input_map, ini_herbs, seed = 1)
c = Cycle(s.object_matrix)


def test_get_adjacent_migratable_cells():
    """should only get migratable cells"""
    migratable_cells  = [type(cell).__name__ for cell in
                       c.get_adjacent_migratable_cells(1, 1)]
    print(migratable_cells)

    # assert migratable_cells == ['Savannah']


def test_food_grows_Savannah():
    """Food amount in each Savannah cell should increase"""

    for row_of_obj in c.object_matrix:
        for obj in row_of_obj:
            if type(obj).__name__ == "Savannah":
                prev_food_sav = obj.f_ij
                c.food_grows()
                assert obj.f_ij > prev_food_sav


def test_max_food_Jungle():
    """When food grows in Jungle cells it should be set to f_max = 800"""

    for row_of_obj in c.object_matrix:
        for obj in row_of_obj:
            if type(obj).__name__ == "Jungle":
                c.food_grows()
                assert obj.f_ij == 800

def test_fitness_increase_after_feeding():
    pass

