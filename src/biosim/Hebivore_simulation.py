# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo
from biosim.Mapping import Cell
#from biosim.Mapping import  Jungle,Savannah, Desert, Ocean, Mountain

class Simulation:
    def __init__(self, island_map, ini_pop, seed = 1,
                 ymax_animals=None, cmax_animals = None,
                 img_base = None, img_fmt='png'):
        """
        :param island_map:
        :param ini_pop:
        :param seed:
        :param ymax_animals:
        :param cmax_animals:
        :param img_base:
        :param img_fmt:
        """
        self.island_map = island_map
        self.ini_pop = ini_pop
        self.seed = seed
        self.animal_object_list = []

        Cell.set_population(self, self.ini_pop)

        Cell.get_population(self)



if __name__ == '__main__':

    g = Geo("""\
        OOOO
        OJJO
        OOOO""")

    ini_herbs = [{'loc': (1, 1), \
                'pop': [{'species': 'Herbivore', \
                'age': 5, \
                'weight': 20} \
                for _ in range(2)] },
                 {'loc': (1, 2), \
                  'pop': [{'species': 'Herbivore', \
                           'age': 5, \
                           'weight': 20} \
                          for _ in range(2)]} ]

    s = Simulation(g, ini_herbs)
    print(s.animal_object_list)




