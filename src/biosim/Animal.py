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
        self.has_migrated = False


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
    has_migrated = False
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
    def herb_eat(self, cell):
        """
        Updates food in the cell object
        Updates the weight of the animal (self)
        :return: None
        """
        if cell.f_ij >= self.p['F']:
            self.weight += self.p['beta'] * self.p['F']
            cell.f_ij -= self.p['F']
        elif cell.f_ij < self.p['F']:
            self.weight += self.p['beta'] * cell.f_ij
            cell.f_ij = 0

    def herb_reproduce(self, length):
        """
        Description
        :param length:
        :return:
        """
        b_prob = min(1, self.p['gamma'] *
                     self.fitness * ( length - 1))

        # 1. check if random_number <= b_prob
        # 2. check if the weight of parent is greater than...
        if (np.random.random() <= b_prob) & \
                (self.weight >= self.p['zeta'] * (
                        self.p['w_birth'] + self.p[
                    'sigma_birth'])):

            baby_weight = np.random.normal(
                self.p['w_birth'], self.p['sigma_birth'])

            # 3. check if animal has sufficient weight
            if self.weight >= baby_weight * self.p['xi']:
                self.weight -= baby_weight * self.p['xi']
                return Herbivore(age=0, weight=baby_weight)

    def herb_migrates(self, cell, adj_cells, proba_list_h):
        """
        Description
        :param cell:
        :param adj_cells:
        :param proba_list_h:
        :return:
        """
        cum_prop = 0
        val = np.random.random()
        for i, prob in enumerate(proba_list_h):
            cum_prop += prob
            if val <= cum_prop:
                new_cell = adj_cells[i]
                new_cell.animal_object_list.append(self)
                break


class Carnivore(Animal):
    """Carnevoir characteristics"""
    has_procreated = False
    has_migrated = False

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

    def carn_eat(self, cell):
        """
        Description
        :param cell:
        :return:
        """
        herb_list = [animal for animal in
                     cell.animal_object_list
                     if type(animal).__name__ == "Herbivore"]
        herb_sorted_rev = sorted(herb_list, key=lambda
            animal: animal.fitness, reverse=True)

        amount_eaten = 0
        dead_list = []

        for ind, herb in enumerate(herb_sorted_rev):
            if self.fitness > herb.fitness:
                if self.fitness - herb.fitness < self.p['DeltaPhiMax']:
                    kill_prob = (self.fitness - herb.fitness) / self.p['DeltaPhiMax']
                    rand_prob = np.random.random()

                    if rand_prob < kill_prob:
                        dead_list.append(ind)

                else:
                    dead_list.append(ind)

        # Delete objects from list
        cell.animal_object_list = [
            animal for idx, animal in enumerate(cell.animal_object_list)
            if idx not in dead_list
        ]

    def carn_reproduce(self, length):
        """
        Description
        :param length:
        :return:
        """
        b_prob = min(1, self.p['gamma'] *
                     self.fitness * ( length - 1))

        # 1. check if random_number <= b_prob
        # 2. check if the weight of parent is greater than...
        if (np.random.random() <= b_prob) & \
                (self.weight >= self.p['zeta'] * (
                        self.p['w_birth'] + self.p[
                    'sigma_birth'])):

            baby_weight = np.random.normal(
                self.p['w_birth'], self.p['sigma_birth'])

            # 3. check if animal has sufficient weight
            if self.weight >= baby_weight * self.p['xi']:
                self.weight -= baby_weight * self.p['xi']
                return Carnivore(age=0, weight=baby_weight)

    def carn_migrates(self, cell, adj_cells, proba_list_c):
        """
        Description
        :param cell:
        :param adj_cells:
        :param proba_list_c:
        :return:
        """
        cum_prop = 0
        val = np.random.random()
        for i, prob in enumerate(proba_list_c):
            cum_prop += prob
            if val <= cum_prop:
                new_cell = adj_cells[i]
                new_cell.animal_object_list.append(self)
                break


if __name__ == "__main__":
    h = Herbivore(5, 10)
    c = Carnivore(5,10)
    print(h.fitness)
    print(c.fitness)