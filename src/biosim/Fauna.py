# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"


# from biosim.Geography import Geo

class Fauna:

    def __init__(self, position, weight, age=0):
        self.age = age
        self.position = position
        self.weight= weight


class Herbivore(Fauna):

    """Herbivores"""
    def __init__(self, position, weight, age=0):
        super().__init__(position, weight, age)
