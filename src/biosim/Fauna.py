# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"


class Fauna:
    def __init__(self, age):
        self.age = age

    def feeding(self):
        pass

    def fitness(self):
        pass

    def migration(self):
        pass

    def procreation(self):
        pass

    def aging(self):
        pass

    def loss_of_weigth(self):
        pass

    def death(self):
        pass


class Herbevoir(Fauna):
    def __init__(self, params_herbs):
        self.params_herbs = params_herbs

        super().__init__()


class Carnevoir(Fauna):
    def __init__(self, params_carn):
        self.params_carn = params_carn

        super().__init__()