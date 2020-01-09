# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo
# from biosim.Fauna import Herbivore
# from biosim.Mapping import Jungle

# from biosim.Mapping import  Jungle,Savannah, Desert, Ocean, Mountain
class Simulation:
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
        self.seed = 1
        self.cell_obj_array = self.island_map.geo_ob_array

        for one_location_list in ini_herbs:
            x, y = one_location_list['loc'][0], one_location_list['loc'][1]
            # set population to the geography at cell(x,y)
            self.cell_obj_array[x][y].set_population(one_location_list)

if __name__ == "__main__":
    map = ("""\
        OOOO
        OJJO
        OOOO""")

    ini_herbs = [ {'loc': (1, 1),
                'pop': [{'species': 'Herbivore',
                'age': 5,
                'weight': 20}
                for _ in range(2)] },
                 {'loc': (1, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(2)]} ]
    # print(ini_herbs)

    s = Simulation(map, ini_herbs)
    cell_obj_array = s.cell_obj_array
    print( cell_obj_array[1][1].animal_object_list)
    print(cell_obj_array[1][1].animal_object_list[1].age )









