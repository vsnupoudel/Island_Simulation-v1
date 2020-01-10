# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Animal import Herbivore, Carnivore


def test_something():

    h = Herbivore(2, 10)
    print(h.age, h.weight, h.fitness)

    c = Carnivore(2, 10)
    print(c.age, c.weight, c.fitness)
    pass
