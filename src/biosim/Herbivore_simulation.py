# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo
from biosim.Cycle import Cycle


class HSimulation:
    def __init__(
            self,
            island_map,
            ini_pop,
            seed=1,
            ymax_animals=None,
            cmax_animals=None,
            img_base=None,
            img_fmt="png",
    ):
        """
        Initialize the map and put animals into the map in the init
        :param island_map: changes string map to a
        :param ini_pop: List of dictionaries specifying initial population
        """
        self.island_map = Geo(island_map)
        self.ini_pop = ini_pop
        # self.seed = 1
        self.object_matrix = self.island_map.object_matrix

        # Set population of animals in the Cell Objects of Geography

        for one_location_list in self.ini_pop:
            x, y = one_location_list['loc'][0], one_location_list['loc'][1]
            # print(x, y)
            # print(one_location_list)
            # set population to the geography at cell(x,y)
            self.object_matrix[x][y].set_population(one_location_list)

    # Call all the functions of Cycle class here every new year

    # Call Cycle.food_grows first

    def call_food_grows(self):
        c1 = Cycle(self.object_matrix)
        c1.food_grows()

    # Secondly call Cycle.animals_eat , Implemented for herbivores only for now

    def call_animal_eats(self):
        c1 = Cycle(self.object_matrix)
        c1.animals_eat()

    # Call Cycle.animals_reproduce , Implemented for herbivores only for now

    def call_animals_reproduce(self):
        c1 = Cycle(self.object_matrix)
        c1.animals_reproduce()


if __name__ == "__main__":
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

    for row, row_of_obj in enumerate(s.object_matrix):
        for col, cell in enumerate(row_of_obj):
            if type(cell).__name__ in  ["Savannah","Jungle"]:
                print ( row,col, type(cell).__name__, "Food is: ", cell.f_ij)

    s.call_food_grows()

    for row, row_of_obj in enumerate(s.object_matrix):
        for col, cell in enumerate(row_of_obj):
            if type(cell).__name__ in  ["Savannah","Jungle"]:
                print ( row,col, type(cell).__name__, "Food is: ", cell.f_ij)

    s.call_animal_eats()

    for row, row_of_obj in enumerate(s.object_matrix):
        for col, cell in enumerate(row_of_obj):
            if type(cell).__name__ in  ["Savannah","Jungle"]:
                print ( row,col, type(cell).__name__, "Food is: ", cell.f_ij)

    for row, row_of_obj in enumerate(s.object_matrix):
        for col, cell in enumerate(row_of_obj):
            if type(cell).__name__ in ["Savannah", "Jungle", "Desert"]:
                print(cell.animal_object_list)

    s.call_animals_reproduce()

    for row, row_of_obj in enumerate(s.object_matrix):
        for col, cell in enumerate(row_of_obj):
            if type(cell).__name__ in ["Savannah", "Jungle", "Desert"]:
                print(cell.animal_object_list)
