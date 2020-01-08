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
    def __init__(self, params_herbs):
        self.params_herbs = params_herbs

        super().__init__()


class Carnevoir(Fauna):
    """Animals with carnevoir characteristics"""
    params_carn = {
        "w_birth": 6.0,
        "sigma_birth": 1.0,
        "beta": 0.75,
        "eta": 0.125,
        "a_half": 60.0,
        "phi_age": 0.4,
        "w_half": 4.0,
        "phi_weight": 0.4,
        "mu": 0.4,
        "lambda": 1.0,
        "gamma": 0.8,
        "zeta": 3.5,
        "xi": 1.1,
        "omega": 0.9,
        "F": 50.0,
        "DeltaPhiMax": 10.0
    }
    def __init__(self, params_carn):
        self.params_carn = params_carn

        super().__init__()