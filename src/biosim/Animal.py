# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import numpy as np
import math

class Animal:
    p = {"w_birth": None,
         "sigma_birth": None,
         "beta": None,
         "eta": None,
         "a_half": None,
         "phi_age": None,
         "w_half": None,
         "phi_weight": None,
         "mu": None,
         "lambda": None,
         "gamma": None,
         "zeta": None,
         "xi": None,
         "omega": None,
         "F": None,
         }
    """Animal characteristics"""

    def __init__(self, param):
        """
        :param param: Dictionary of paramerters for animals
        """
        self.p = param


    @property
    def fitness(self):
        """The fitness of each animal"""
        if self.weight <= 0:
            return 0
        else:
            return (1 / (1 + math.e ** (self.p['phi_age'] * (
                    self.age - self.p['a_half'])))) * (1 / (1 + math.e **\
                (- self.p['phi_weight'] * (self.weight - self.p['w_half']))))


    @classmethod
    def up_par(cls, params_dict):
         """
         :param params_dict: Dictionary of parameters to be updated
         """

         for k, v in params_dict.items():
             if k not in cls.p:
                 print('ValueError')
             if v <= 0:
                 print('ValueError')

         cls.p.update(params_dict)


class Herbivore(Animal):
    """Herbivore characteristics, subclass of Animal class"""
    has_procreated = False
    p = {"w_birth": 8.0,
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
         "DeltaPhiMax": None}

    def __init__(self, age, weight):

        self.weight = weight
        self.age = age
        self.is_dead = False



        if self.weight is None:
            self.weight = np.random.normal(self.p['w_birth'],
                                           self.p[
                                               'sigma_birth'])


class Carnivore(Animal):
    """Carnevoir characteristics"""
    has_procreated = False

    p = {
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

    def __init__(self, age, weight):
        self.age = age
        self.weight = weight
        self.is_dead = False

        if self.weight is None:
            self.weight = np.random.normal(self.p['w_birth'],
                                           self.p['sigma_birth'])




if __name__ == "__main__":
    h = Herbivore(5, 10)
    c = Carnivore(5,10)
    print(h.fitness)
    print(c.fitness)