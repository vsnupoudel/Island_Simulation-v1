# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Herbivore_simulation import HSimulation


def test_carnivores_eat():
    map = ("""\
         OOOOO
         OJSDO
         OJSMO
         OJSDO
         OOOOO""")
    ini_herbs = [{'loc': (1, 1), 'pop': [{'species': 'Herbivore', 'age': 20,
                                          'weight': 5} for _ in range(100)] + [
                                            {'species': 'Carnivore', 'age': 10,
                                             'weight': 500}
                                        ]}]

    s = HSimulation(map, ini_herbs)

    original_animals_number = len(s.object_matrix[1][1].animal_object_list)
    print( "original_animals_number:", original_animals_number)

    s.call_animal_eats()

    new_animals_number = len(s.object_matrix[1][1].animal_object_list)
    print("new_animals_number:", new_animals_number)

    assert new_animals_number < original_animals_number

def test_weights_after_eating():
    pass
