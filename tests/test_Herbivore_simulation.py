# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Herbivore_simulation import HSimulation


def test_check_food_grows_and_animals_eat():
    """
    For this test to work, he default values should be
    Savannah: f_ij=200, f_max = 300 ,alpha=0.3
    Jungle : f_ij=300, f_max = 800,  alpha=0.3
    """
    map = ("""\
            OOOOO
            OJSDO
            OJSMO
            OJSDO
            OOOOO""")
    ini_herbs = [{'loc': (1, 1), 'pop': [{'species': 'Herbivore', 'age': 5,
                                          'weight': 20} for _ in range(2)]},
                 {'loc': (1, 2), 'pop': [{'species': 'Herbivore', 'age': 5,
                                          'weight': 20} for _ in range(2)]}]

    # create a map with initial population
    s = HSimulation(map, ini_herbs)

    # grow food in Jungle and Savannah
    s.call_food_grows()

    # Check if the food grew
    food_matrix = []
    for row, row_of_obj in enumerate(s.object_matrix):
        food_row = []
        for col, cell in enumerate(row_of_obj):
            if type(cell).__name__ in ["Savannah", "Jungle"]:
                food_row.append(cell.f_ij)
            else:
                food_row.append(0)
        food_matrix.append(food_row)

    assert food_matrix == [[0, 0, 0, 0, 0],
                           [0, 800, 230.0, 0, 0],
                           [0, 800, 230.0, 0, 0],
                           [0, 800, 230.0, 0, 0],
                           [0, 0, 0, 0, 0]]

    # Make animals eat
    s.call_animal_eats()

    # Check if the animals ate
    food_matrix = []
    for row, row_of_obj in enumerate(s.object_matrix):
        food_row = []
        for col, cell in enumerate(row_of_obj):
            if type(cell).__name__ in ["Savannah", "Jungle"]:
                food_row.append(cell.f_ij)
            else:
                food_row.append(0)
        food_matrix.append(food_row)

    assert food_matrix == [[0, 0, 0, 0, 0],
                           [0, 780.0, 210.0, 0, 0],
                           [0, 800, 230.0, 0, 0],
                           [0, 800, 230.0, 0, 0],
                           [0, 0, 0, 0, 0]]

def test_animals_reproduce():
    map = ("""\
        OOOOO
        OJSDO
        OJSMO
        OJSDO
        OOOOO""")
    ini_herbs = [{'loc': (1, 1), 'pop': [{'species': 'Herbivore', 'age': 6,
                                          'weight': 25},
                                         {'species': 'Herbivore', 'age': 7,
                                          'weight': 30}]},
                 {'loc': (1, 2), 'pop': [{'species': 'Herbivore', 'age': 5,
                                          'weight': 100} for _ in range(10)]}]

    s = HSimulation(map, ini_herbs)
    s.call_food_grows()
    s.call_animal_eats()

    for row, row_of_obj in enumerate(s.object_matrix):
        for col, cell in enumerate(row_of_obj):
            if type(cell).__name__ in ["Savannah", "Jungle", "Desert"]:
                print(cell.animal_object_list)

    s.call_animals_reproduce()

    for row, row_of_obj in enumerate(s.object_matrix):
        for col, cell in enumerate(row_of_obj):
            if type(cell).__name__ in ["Savannah", "Jungle", "Desert"]:
                print(cell.animal_object_list)

    assert (len(s.object_matrix[1][2].animal_object_list) > 10) &  (len(
        s.object_matrix[1][1].animal_object_list) >= 2)

def test_both_reproduce():
    map = ("""\
           OOOOO
           OJSDO
           OJSMO
           OJSDO
           OOOOO""")
    ini_herbs = [{'loc': (1, 1), 'pop': [{'species': 'Herbivore', 'age': 5,
                                          'weight': 100} for _ in range(6)] + [
                                            {'species': 'Carnivore', 'age': 10,
                                             'weight': 500} for _ in range(2)
                                        ]}]

    s = HSimulation(map, ini_herbs)

    herb_length = 0
    carn_length = 0

    for row, row_of_obj in enumerate(s.object_matrix):
        for col, cell in enumerate(row_of_obj):
            if (row == 1) & (col == 1):
                for animal in cell.animal_object_list:
                    if type(animal).__name__ == "Herbivore":
                        herb_length += 1
                    else:
                        carn_length += 1
                        # print(cell.animal_object_list)

    s.call_animals_reproduce()

    herb_length_after = 0
    carn_length_after = 0

    for row, row_of_obj in enumerate(s.object_matrix):
        for col, cell in enumerate(row_of_obj):
            if (row == 1) & (col == 1):
                for animal in cell.animal_object_list:
                    if type(animal).__name__ == "Herbivore":
                        herb_length_after += 1
                    else:
                        carn_length_after += 1

    assert (herb_length_after > herb_length) & (
            carn_length_after > carn_length)



