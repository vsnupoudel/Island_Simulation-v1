# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"


from biosim.Geography import Geo


class Fauna:

    def __init__(self, position, weigth, age=0):

        self.age = age
        self.position = position
        self.weigth= weigth


class Herbivore(Fauna):

    """Herbivores"""
    def __init__(self, position, weight, age=0):
        super().__init__(position, weight, age)


if __name__ == "__main__":
    g = Geo("""\
       OOOOOOOOOOOOOOOOOOOOO
       OOOOOOOOJMMMMJJJJJJJO
       OSSSSSJJJJJJJJJJJJJOO
       OOOOOOOOOOOOOOOOOOOOO""")

    ini_herbs = {'loc': (10, 10), \
                'pop': [{'species': 'Herbivore', \
                'age': 5, \
                'weight': 20} \
                for _ in range(150)] }
    print(ini_herbs['loc'])
    print(ini_herbs['pop'][149])
    # print(ini_herbs[0])
    # print(ini_herbs['pop'])

    # for row_num, row_list in enumerate(g.geo_ob_array):
    #     print(row_num,row_list)
    #     for column_num, obj in enumerate(row_list):
    #         if obj.is_migratable:
    #             H = Herbivore((row_num,column_num), type(obj).__name__ )
    #             print (H.age)

