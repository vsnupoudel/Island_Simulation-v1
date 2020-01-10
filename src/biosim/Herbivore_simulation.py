# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo
from biosim.Cycle import Cycle
from biosim.Eat import Eat


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
        self.cell_obj_array = self.island_map.geo_ob_array

        for one_location_list in self.ini_pop:
            x, y = one_location_list['loc'][0], one_location_list['loc'][1]
            print(x,y)
            print(one_location_list)
            # set population to the geography at cell(x,y)
            self.cell_obj_array[x][y].set_population(one_location_list)

    def simulate(self, num_years, vis_years=1, img_years= None):
        pass
    # Call all the functions of Cycle class here every new year

if __name__ == "__main__":
    map = ("""\
        OOOO
        OJJO
        OOOO""")
    ini_herbs = [ {'loc': (1, 1),
                'pop': [{'species': 'Herbivore',
                'age': 5,
                'weight': 20}
                for _ in range(2)] }, {'loc': (1, 2),
                'pop': [{'species': 'Herbivore',
                'age': 5,
                'weight': 20}
                for _ in range(2)] }]

    s = HSimulation (map, ini_herbs)

    cycle = Cycle(s.cell_obj_array)
    cycle.animals_eat()
    # print(s.cell_obj_array)

    # jungle_object = s.cell_obj_array[1][1]
    # print(jungle_object)
    # print(jungle_object.f_ij)
    #
    # print(jungle_object.get_population()[0])
    # print( jungle_object.get_population()[0].weight )
    # #make it eat
    # e = Eat()
    # e.herb_eat(jungle_object, jungle_object.get_population()[0])
    # # after eating
    #
    # print(jungle_object.f_ij)
    # print(jungle_object.get_population()[0].weight)
