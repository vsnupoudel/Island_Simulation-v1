# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo
from biosim.Mapping import Jungle, Savannah


class Simulation:
    def __init__(self):
        pass

    def food_grows(self, input_map):
        map = Geo(input_map)
        print(map.geo_ob_array)

        for row_of_obj in map.geo_ob_array:
            for obj in row_of_obj:

                if type(obj).__name__ == "Savannah":
                    # print(obj)
                    # print(obj.f_ij, obj.f_max)
                    obj.f_ij += obj.alpha * (obj.f_max - obj.f_ij)
                    # print(obj.f_ij, obj.f_max)
                elif type(obj).__name__ == "Jungle":
                    # print(obj)
                    # print(obj.f_ij, obj.f_max)
                    obj.f_ij = obj.f_max
                    # print(obj.f_ij, obj.f_max)


if __name__ == "__main__":
    si = Simulation()
    input_map = ("""\
                    OOOO
                    OJSO
                    OOOO""")

    si.food_grows(input_map)


