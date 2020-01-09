#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Anders Huse, Bishnu Poudel'
__email__ = 'anhuse@nmbu.no; bipo@nmbu.no'

from biosim.Fauna import Herbivore

# import numpy as np

class Cell:
    """Super class for the type of Terrain"""

    def __init__(self, row, column):
        """
        :param row: row index
        :param column: column index
        """
        self.row = row
        self.column = column

    def set_population(self, input_list):
        """
        Sets the animals species, age and weight
                :param input_dict: with species,age, weight
                """
        self.pop_list = input_list

        for animal in self.pop_list:
            (x, y) = animal['loc']
            print(x,y)

            animal_list = []
            for spes in animal['pop']:
                animal_list.append((spes['species']))
                print(animal_list)

 #           for spes in animal['pop']:
#                l.append((spes['species']))

    def get_population(self):
        return self.pop_list


class Jungle(Cell):
    f_max = 800
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
        :param f_ij: food in cell
        :param alpha: calculation parameter
        :param num_carn: number of carnevoirs in cell
        :param num_herb: number og herbevoirs in cell
        """
        super().__init__(row, column)
        self.food = f_ij
        self.alpha = alpha
        # self.num_carn = None
        # self.num_herb = None
        # self.herb_list = []
        # self.carn_list =[]


class Savannah(Cell):
    f_max = 300
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
        :param f_ij: food in cell
        :param alpha: calculation parameter
        :param num_carn: number of carnevoirs in cell
        :param num_herb: number og herbevoirs in cell
        """

        super().__init__(row, column)
        self.food = f_ij
        self.aplha = alpha
        # self.num_carn = num_carn
        # self.num_herb = num_herb
        self.herb_list = []
        self.carn_list =[]


class Desert(Cell):
    """Desert landscape"""

    is_migratable = True
    f_max = 0

    def __init__(
            self,
            row,
            column,
            # num_carn=0,
            # num_herb=0,
            f_ij=f_max,
    ):
        """"
        :param f_ij: food in cell
        :param num_carn: number of carnevoirs in cell
        :param num_herb: number og herbevoirs in cell
        """

        super().__init__(row, column)
        self.food = f_ij
        # self.num_herb = num_herb
        # self.num_carn = num_carn
        self.herb_list = []
        self.carn_list =[]
# [H,H,H,H,H]

class Ocean(Cell):
    """Ocean landscape """
    is_migratable = False
    def __init__(self, row, column):
        super().__init__(row, column)

class Mountain(Cell):
    """Mountianlandscape"""
    is_migratable = False
    def __init__(self, row, column):
        super().__init__(row, column)


if __name__ == '__main__':
    j = Jungle(2, 3)
    # print(j.row, j.column, j.is_migratable)
  #  j.set_population([{'species': 'Herbivore', 'age': 5, 'weight': 20}, {'species': 'Herbivore', 'age': 5, 'weight': 20}])
  #  print(j.get_population())

    a = [{'loc': (10, 10), 'pop': [{'species': 'Herbivore', 'age': 5, 'weight': 20},{'species': 'Herbivore', 'age': 5, 'weight': 20}]}]

    j.set_population(a)
