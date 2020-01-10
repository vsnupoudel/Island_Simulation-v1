# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import numpy as np
import math
import random


#from biosim.Mapping import Jungle

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
        self.input_param_dict = param  # These are entered by users


    @property
    def fitness(self):
        """The fitness of each animal"""
        if self.weight <= 0:
            return 0
        else:
            return (1 / (1 + math.e ** (self.p['phi_age'] * (
                    self.age - self.p['a_half'])))) * (1 / (1 + math.e ** (- self.p['phi_weight'] * (self.weight - self.p['w_half']))))

    # def give_birth(self, N):
    #     """
    #     Birth
    #     :input_param_dict N: Number of animals of same species in one cell
    #     :return: new_born_weigth
    #     """
    #
    #     if (N <= 1) & (self.weigth < self.p['xi'] * (
    #             self.p['w_birth'] + self.p['sigma_birth'])):
    #         has_procreated = False
    #
    #     birth_prob = min(1, self.p['gamma'] * self.fitness * (N - 1))
    #     num = np.random.random()
    #     print(num, birth_prob)
    #
    #     has_procreated = num <= birth_prob
    #
    #     new_born_weight = np.random.normal(self.p['w_birth'],
    #                                        self.p['sigma_birth'])
    #
    #     if self.weigth - self.p['xi'] * new_born_weight <= 0:
    #         has_procreated = False
    #
    #     if has_procreated:
    #         self.weigth -= self.p['xi'] * new_born_weight
    #
    #     return new_born_weight

    # then create new animal

    # call weigth method

    def up_par(self, params_dict):
         """
         Updates animal parameters
         :input_param_dict params_dict: dictionary of parameters
         """

         for k, v in params_dict.items():
             if k not in self.p:
                 print('ValueError')
             if v <= 0:
                 print('ValueError')

         self.p.update(params_dict)


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
            self.weight = np.random.normal(self.output_param_dict['w_birth'],
                                           self.output_param_dict[
                                               'sigma_birth'])
        if self.is_dead:
            #remove animal
            pass

class Carnivore(Animal):
    """Carnivore characteristics"""
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

        self.weight = weight
        self.age = age
        self.is_dead = False

        if self.weight is None:
            self.weight = np.random.normal(self.p['w_birth'],
                                           self.p['sigma_birth'])

        if self.is_dead:
            #remove animal
            pass


if __name__ == "__main__":

#    h = Herbivore(2, 10)
#    print(h.age, h.weight, h.fitness)
#
#    c = Carnivore(2,10)
#    print(c.age, c.weight, c.fitness)

    ini_herbs = [{'loc': (1, 1),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(2)]},]

    j = Jungle(1,1)
    j.set_population(ini_herbs)
    j.get_population()