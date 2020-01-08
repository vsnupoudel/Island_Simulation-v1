# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo

class Fauna:
    def __init__(self, age, position, Land_type):
        self.age = age
        self.position = position
        self.Land_type= Land_type


class Herbevoir(Fauna):
    """Animals with herbevoir characteristics"""
    params_herb = {
        "w_birth": 8.0,
        "sigma_birth": 1.5,
        "beta": 0.9,
        "eta": 0.05,
        "a_half": 40.0,
        "phi_age": 0.2,
        "w_half": 10.0,
        "phi_weight": 0.1,
        "mu": 0.25,
        "lambda": 1.0,
        "gamma": 0.2,
        "zeta": 3.5,
        "xi": 1.2,
        "omega": 0.4,
        "F": 10.0,
    }
    def __init__(self, age, position, Land_type):
        # self.params_herbs = params_herbs
        super().__init__()


if __name__ == "__main__":
    g = Geo("""\
       OOOOOOOOOOOOOOOOOOOOO
       OOOOOOOOJMMMMJJJJJJJO
       OSSSSSJJJJJJJJJJJJJOO
       OOOOOOOOOOOOOOOOOOOOO""")
