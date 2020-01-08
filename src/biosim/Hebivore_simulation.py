# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo
from biosim.Mapping import  Jungle,Savannah, Desert, Ocean, Mountain

g = Geo("""\
    OOO
    OJO
    OOO""")

ini_herbs = {'loc': (1, 1), \
            'pop': [{'species': 'Herbivore', \
            'age': 5, \
            'weight': 20} \
            for _ in range(150)] }
print(ini_herbs['loc'])
print(ini_herbs['pop'][149])

