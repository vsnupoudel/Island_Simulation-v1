#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Anders Huse, Bishnu Poudel'
__email__ = 'anhuse@nmbu.no; bipo@nmbu.no'

from Animal import Herbivore, Carnivore
import numpy as np
import math


class Cell:
    """
    Super class for the type of Terrain: Jungle, Savannah, Desert,
    Ocean or Mountain.

    Attributes:
        row:                  int, row index of the position of the cell
        column:               int, column index of the position of the cell
        f_ij:                 float(default=0), food avilable in each cell
        alpha:                float(default=0.3), parameter
        animal_object_list:   list, list of animal objects
        tot_herb_weight:      float, total weigth of all herbivores in a cell
        rel_ab_carn:          float, relative abundance of fodder for carnivores
        rel_ab_herb:          float, relative abundance of fodder for herbivores

    """

    def __init__(self, row, column, f_ij=0, alpha=0.3):
        """
        :param row:    int, row index of the position of the cell
        :param column: int, column index of the position of the cell
        :param f_ij:   float(default=0), food avilable in each cell
        :param alpha:  float(default=0.3), parameter
        """
        self.row = row
        self.column = column
        self.animal_object_list = []
        self.f_ij = f_ij
        self.alpha = alpha
        self.animal_object_list = []

        self.tot_herb_weight = np.sum([a.weight for a in self.herb_list])

        self.rel_ab_carn = self.tot_herb_weight / (self.n_carns + 1) * \
                           Carnivore.p['F']
        self.rel_ab_herb = self.f_ij / (self.n_herbs + 1) * Herbivore.p['F']


    @property
    def pi_ij_carn(self):
        """propensity for a cell object for carnivores"""
        return math.e ** (Carnivore.p['lambda'] * self.rel_ab_carn)

    @property
    def pi_ij_herb(self):
        """propensity for a cell object for herbivores"""
        return math.e ** (Herbivore.p['lambda'] * self.rel_ab_herb)

    def set_population(self, input_dict):
        """
        Sets the population of a cell object
        :param input_dict: dict, dictionary specifying the population to be
        set for the cell object, containing:
        location of cell object, type of animals, age and weight of animals
        """
        (x, y) = input_dict['loc']
        for animal in input_dict['pop']:
            if animal['species'] == "Herbivore":
                self.animal_object_list.append(Herbivore(age=animal[
                    'age'], weight=animal['weight']))
            else:
                self.animal_object_list.append(Carnivore(age=animal[
                    'age'], weight=animal['weight']))

    def get_population(self):
        """
        :return: animal_object_list
        """
        return self.animal_object_list

    @property
    def herb_list(self):
        """List of all herbivore objects in the cell object"""
        return [a for a in self.animal_object_list
                      if type(a).__name__ == "Herbivore"]

    @property
    def herb_sorted(self):
        """Sorted list of all herbivore objects in the cell object"""
        return sorted(self.herb_list, key=lambda animal: animal.fitness)

    @property
    def herb_sorted_rev(self):
        """Reversed-sorted list of all herbivore objects in the cell object"""
        return sorted(self.herb_list, key=lambda animal: animal.fitness,
                             reverse=True)

    @property
    def carn_list(self):
        """List of all carnivore objects in the cell object"""
        return [a for a in self.animal_object_list
                      if type(a).__name__ == "Carnivore"]

    @property
    def carn_sorted(self):
        """Sorted list of all carnivore objects in the cell object"""
        return sorted(self.carn_list, key=lambda animal: animal.fitness,
                         reverse=True)

    @property
    def n_herbs(self):
        """Number of herbivore objects in the cell object"""
        return len(self.herb_list)

    @property
    def n_carns(self):
        """Number of carnivore objects in the cell object"""
        return len(self.carn_list)


class Jungle(Cell):
    """
    Jungle landscape. Child class of the Cell class.

    Attributes:
        parameters:           dict, dictionary of Jungle parameters,
                                    containing:
                                    f_max: int, maximal available food in
                                                Jungle object
                                    alpha: (default, None), parameter
        is_migratable         bool(default, True), whether the cell is
                                                   migratable or not for
                                                   animal objects
        row:                  int, row index of the position of the cell
        column:               int, column index of the position of the cell
        f_ij:                 float(default=300), food avilable in each cell
        alpha:                (default=None), parameter
        animal_object_list:   list, list of animal objects
        tot_herb_weight:      float, total weigth of all herbivores in a cell
        rel_ab_carn:          float, relative abundance of fodder for carnivores
        self.rel_ab_herb:     float, relative abundance of fodder for herbivores

    """
    parameters = {'f_max': 800.0, 'alpha': None}
    is_migratable = True

    def __init__(
            self,
            row,
            column,
            # num_carn=0,
            # num_herb=0,
            f_ij=300,
            alpha=0.3,
    ):
        """
        :param row:    int, row index of the position of the cell
        :param column: int, column index of the position of the cell
        :param f_ij:   float(default=300), food avilable in each cell
        :param alpha:  float(default=0.3), parameter
        """
        super().__init__(row, column)
        self.f_ij = f_ij
        self.alpha = alpha


class Savannah(Cell):
    """
    Savannah landscape. Child class of the Cell class.

    Attributes:
        parameters:           dict, dictionary of Jungle parameters,
                                    containing:
                                    f_max: int, maximal available food in
                                                Jungle object
                                    alpha: (default, None), parameter
        is_migratable         bool(default, True), whether the cell is
                                                   migratable or not for
                                                   animal objects
        row:                  int, row index of the position of the cell
        column:               int, column index of the position of the cell
        f_ij:                 float(default=200), food avilable in each cell
        alpha:                float(default=0.3), parameter
        animal_object_list:   list, list of animal objects
        tot_herb_weight:      float, total weigth of all herbivores in a cell
        rel_ab_carn:          float, relative abundance of fodder for carnivores
        self.rel_ab_herb:     float, relative abundance of fodder for herbivores

    """
    parameters = {'f_max': 800.0, 'alpha': None}
    is_migratable = True

    def __init__(
            self,
            row,
            column,
            f_ij=200,
            alpha=0.3,
    ):
        """
        :param row:    int, row index of the position of the cell
        :param column: int, column index of the position of the cell
        :param f_ij:   float(default=200), food avilable in each cell
        :param alpha:  float(default=0.3), parameter
        """

        super().__init__(row, column)
        self.f_ij = f_ij
        self.alpha = alpha


class Desert(Cell):
    """
    Desert landscape. Child class of the Cell class.

    Attributes:
        is_migratable         bool(default, True), whether the cell is
                                                   migratable or not for
                                                   animal objects
        row:                  int, row index of the position of the cell
        column:               int, column index of the position of the cell
        animal_object_list:   list, list of animal objects
        tot_herb_weight:      float, total weigth of all herbivores in a cell
        rel_ab_carn:          float, relative abundance of fodder for carnivores
        self.rel_ab_herb:     float, zero for desert landscape

    """
    is_migratable = True

    def __init__(
            self,
            row,
            column
            # num_carn=0,
            # num_herb=0,
    ):
        """"
        :param row:    int, row index of the position of the cell
        :param column: int, column index of the position of the cell
        """
        super().__init__(row, column)


class Ocean(Cell):
    """Ocean landscape. Child class of the Cell class.

        Attributes:
        is_migratable         bool(default, False), whether the cell is
                                                   migratable or not for
                                                   animal objects
        row:                  int, row index of the position of the cell
        column:               int, column index of the position of the cell

    """
    is_migratable = False

    def __init__(self, row, column):
        """"
        :param row:    int, row index of the position of the cell
        :param column: int, column index of the position of the cell
        """
        super().__init__(row, column)


class Mountain(Cell):
    """Mountian landscape.  Child class of the Cell class.

        Attributes:
        is_migratable         bool(default, False), whether the cell is
                                                   migratable or not for
                                                   animal objects
        row:                  int, row index of the position of the cell
        column:               int, column index of the position of the cell

    """
    is_migratable = False

    def __init__(self, row, column):
        """"
        :param row:    int, row index of the position of the cell
        :param column: int, column index of the position of the cell
        """
        super().__init__(row, column)

