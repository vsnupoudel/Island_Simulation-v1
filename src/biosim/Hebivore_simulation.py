# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo
from biosim.Mapping import  Jungle,Savannah, Desert, Ocean, Mountain


g = Geo("""\
    OOOO
    OJJO
    OOOO""")
print( g.geo_ob_array[1][1])
print( g.geo_ob_array[1][2])
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

g.geo_ob_array[1][1]).set_population(ini_herbs[0]['pop'])

# print(ini_herbs[0]['loc'])
# print(ini_herbs[0]['pop'])
# print(ini_herbs[0]['pop'])
# print(ini_herbs[0]['pop'][1] )
# print(ini_herbs[0]['pop'][1]['species'] )





