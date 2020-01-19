# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import numpy as np
import math
# import functools
#from cached_property import cached_property


class Animal:
    """
    SuperClass for Herbivore and Carnivore.
    Contains methods, properties and variables that are common in both.

        Attributes:

        p:                   dict, dictionary of parameters for the
                                          animal objects. All parameters are
                                          None by default

        has_procreated:       bool(default, False), whether the animal object
                                                    has procreated or not
        has_migrated:         bool(default, False), whether the animal object
                                                    has migrated or not
        is_dead:              bool(default, False), whether the animal object
                                                    is dead or alive
        age:                  int, the age of the animal
        weight:               float, the weight of the animal
        reprod_thresh_weight:  float, treshold weight for reproduction
    """
    has_procreated = False
    has_migrated = False
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

    def __init__(self, age, weight):
        """
        :param age:    int, the age of the animal
        :param weight: float, the weight of the animal
        """
        self.weight = weight
        self.age = age
        self.is_dead = False

        if self.weight is None:
            self.weight = np.random.normal(self.p['w_birth']
                                           , self.p['sigma_birth'])
        self.has_migrated = False

        self.reprod_thresh_weight = self.p['zeta'] * (self.p['w_birth'] +
                                                    self.p['sigma_birth'])

    @property
    def fitness(self):
        """The fitness of each animal"""
        if self.weight <= 0:
            return 0
        else:

            return (1 / (1 + math.e ** (self.p['phi_age'] * (
                    self.age - self.p['a_half']))))  \
                   * (1 / (1 + math.e **(- self.p['phi_weight'] * (
                    self.weight - self.p['w_half']))))

    @property
    def move_prob(self):
        return self.p['mu'] * self.fitness

    @property
    def death_prob(self):
        return self.p['omega'] * (1 - self.fitness)

    @classmethod
    def up_par(cls, params_dict):
        """
        Updates the animal parameters
        :param params_dict: Dictionary of parameters to be updated
        """
        for k, v in params_dict.items():
            if k not in cls.p:
                raise ValueError(k, ' is an invalid Key')
            if v <= 0:
                raise ValueError(k, v, ' Param value must be positive')

        cls.p.update(params_dict)


class Herbivore(Animal):
    """Herbivore characteristics, subclass of Animal class

        Attributes:

        p:                   dict, dictionary of parameters for the Herbivore
                                   objects.

        has_procreated:       bool(default, False), whether the animal object
                                                    has procreated or not
        has_migrated:         bool(default, False), whether the animal object
                                                    has migrated or not
        is_dead:              bool(default, False), whether the animal object
                                                    is dead or alive
        age:                  int, the age of the animal
        weight:               float, the weight of the animal
        reprod_thresh_weight  float, treshold weight for reproduction
    """


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
        """
        :param age:    int, the age of the animal
        :param weight: float, the weight of the animal
        """
        super().__init__(age,weight)

    def herb_eat(self, cell):
        """
        Herbivores eat. This method updates the amount of food in the cell
        object and the weight of the animal.
        :param cell:   Cell object, the cell where this animal resides.
        """
        if cell.f_ij >= self.p['F']:
            self.weight += self.p['beta'] * self.p['F']
            cell.f_ij -= self.p['F']
        elif cell.f_ij < self.p['F']:
            self.weight += self.p['beta'] * cell.f_ij
            cell.f_ij = 0

    def herb_reproduce(self, length):
        """
        Reproduction for herbivores. The weight of the mother animal decreases
        when it gives birth.
        :param length: int, number of total herbivores in the cell where the
                            herbivore resides
        :return: A baby herbivore object with age = 0 and weight equal to
        baby weight
        """

        b_prob = min(1, self.p['gamma'] *
                     self.fitness * (length - 1))

        # 1. Probability condition is satisfied if random_number <= b_prob
        # 2. check if the weight of parent is greater than threshold

        if (np.random.random() <= b_prob) & \
                (self.weight >= self.reprod_thresh_weight):

            baby_weight = np.random.normal(
                self.p['w_birth'], self.p['sigma_birth'])

            # 3. check if animal loses more than the baby's weight
            if self.weight >= baby_weight * self.p['xi']:
                self.weight -= baby_weight * self.p['xi']
                return Herbivore(age=0, weight=baby_weight)

    def herb_migrates(self, animal, cell, adj_cells, proba_list_h):
        """
        Herbivore migrates. This method decides which cell the animal migrates
        to, of the adjacent cells to the current cell.
        :param animal:       Herbivore object, the herbivore object that is
                                               chosen to move
        :param cell:         Cell object, the current cell
        :param adj_cells:    list, a list consisting of the adjacent cell
                                   objects
        :param proba_list_h: list, a list with probabilities corresponding to
                                   the list of adjacent cells
        :return: None
        """
        cum_prop = 0
        val = np.random.random()
        for i, prob in enumerate(proba_list_h):
            cum_prop += prob
            if val <= cum_prop:
                new_cell = adj_cells[i]
                new_cell.animal_object_list.append(animal)
                break


class Carnivore(Animal):
    """Carnivore characteristics, subclass of Animal class

        Attributes:

        p:                   dict, dictionary of parameters for the Carnivore
                                   objects.

        has_procreated:       bool(default, False), whether the animal object
                                                    has procreated or not
        has_migrated:         bool(default, False), whether the animal object
                                                    has migrated or not
        is_dead:              bool(default, False), whether the animal object
                                                    is dead or alive
        age:                  int, the age of the animal
        weight:               float, the weight of the animal
        reprod_thresh_weight  float, treshold weight for reproduction
    """
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
        """
        :param age:    int, the age of the animal
        :param weight: float, the weight of the animal
        """
        super().__init__(age, weight)

    def carn_eat(self, cell):
        """
        Carnivores eat
        When Carnivores eat, this method:
        - delete herbivores from the cell after they are eaten.
        - Update the weight of carnivore when they have eaten.

        Conditions for a carnivore eating are:
        1. They eat until they get an amount F (yet to implement ??)
        2. If fitness is less than a herbivore, they can't kill that herbivore
        3. They kill with certain probability, if they have less than
        DeltaPhiMax fitness
        4. They certainly kill that herbivore otherwise
        :param cell:   Cell object, The cell object where the carnivore resides
        :return :None
        """
        amount_eaten = 0

        dead_list = []
        for herb in cell.herb_sorted_rev:
            if self.fitness > herb.fitness:
                if self.fitness - herb.fitness < self.p['DeltaPhiMax']:
                    kill_prob = (self.fitness - herb.fitness) / self.p[
                        'DeltaPhiMax']
                    rand_prob = np.random.random()

                    if rand_prob < kill_prob:
                        dead_list.append(herb)
                        amount_eaten += herb.weight
                        self.weight += self.p['beta']*herb.weight
                else:
                    dead_list.append(herb)
                    amount_eaten += herb.weight
                    self.weight += self.p['beta']*herb.weight

            # Check if the carnivore is satisfied yet
            if amount_eaten > self.p['F']:
                break

        # Delete killed herbivores from list in the cell/update the list
        cell.animal_object_list = [
            animal for animal in cell.animal_object_list
            if animal not in dead_list]


    def carn_reproduce(self, length):
        """
        Reproduction for carnivores
        :param length:               int, number of total carnivores in the
                                          cell where the herbivore resides
        :return: A baby carnivores   Carnivore object (with age=0 and weight
                                     equal to baby weight)
        """

        b_prob = min(1, self.p['gamma'] *
                     self.fitness * (length - 1))

        # Probability condition is satisfied if random_number <= b_prob
        # check if the weight of parent is greater than threshold

        if (np.random.random() <= b_prob) & \
                (self.weight >= self.reprod_thresh_weight):

            baby_weight = np.random.normal(
                self.p['w_birth'], self.p['sigma_birth'])

            # 3. check if animal loses more than the baby's weight
            if self.weight >= baby_weight * self.p['xi']:
                self.weight -= baby_weight * self.p['xi']
                return Carnivore(age=0, weight=baby_weight)

    def carn_migrates(self, animal, cell, adj_cells, proba_list_c):
        """
        Carnivore migrates. This method decides which cell the animal migrates
        to, of the adjacent cells to the current cell.
        :param animal:       Carnivore object, the carnivore object that is
                                               chosen to move
        :param cell:         Cell object, the current cell
        :param adj_cells:    list, a list consisting of the adjacent cell
                                   objects
        :param proba_list_h: list, a list with probabilities corresponding to
                                   the list of adjacent cells
        :return: None
        """
        cum_prop = 0
        val = np.random.random()

        for i, prob in enumerate(proba_list_c):
            cum_prop += prob
            if val <= cum_prop:
                new_cell = adj_cells[i]
                new_cell.animal_object_list.append(animal)
                break
