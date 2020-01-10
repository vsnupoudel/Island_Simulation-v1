# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo
from biosim.Mapping import Jungle, Savannah


class Cycle:
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

    # for hver celle:
    def animals_eat(self, map):
        """Herbevoirs and Carnevoirs eat"""

        for row_of_obj in map.geo_ob_array:
            for cell in row_of_obj:
                herb_sorted = sorted(cell.herb_list, key=lambda animal: animal.fitness,
                                 reverse=True)

        for herb in herb_sorted:
            if herb.p['F'] <= cell.f_ij:
                herb.weight += herb.p['beta'] * herb.p['F']
                cell.f_ij -= herb.p['F']

        # carn_sorted = sorted(cell.carn_list, key=lambda animal: animal.fitness,
        #                      reverse=True)
        #
        # for c in carn_sorted:
        #     c.carn_eat()


if __name__ == "__main__":
    si = Cycle()
    input_map = ("""\
                    OOOO
                    OJSO
                    OOOO""")

    si.food_grows(input_map)


