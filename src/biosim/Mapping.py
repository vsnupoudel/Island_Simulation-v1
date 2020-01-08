#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Anders Huse, Bishnu Poudel'
__email__ = 'anhuse@nmbu.no; bipo@nmbu.no'


# import numpy as np

class Map:
    """Super class for the type of Terrain"""

    def __init__(self, row, column):
        """
        :param row: row index
        :param column: column index
        """
        self.row = row
        self.column = column


class Jungle(Map):
    f_max = 800
    migratable = True

    def __init__(
            self,
            row,
            column,
            num_carn=0,
            num_herb=0,
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
        self.num_carn = num_carn
        self.num_herb = num_herb


class Savannah(Map):
    f_max = 300
    is_migratable = True

    def __init__(
            self,
            row,
            column,
            num_carn=0,
            num_herb=0,
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
        self.num_carn = num_carn
        self.num_herb = num_herb


class Desert(Map):
    """Desert landscape"""

    migratable = True
    f_max = 0

    def __init__(
            self,
            row,
            column,
            num_carn=0,
            num_herb=0,
            f_ij=f_max,
    ):
        """"
        :param f_ij: food in cell
        :param num_carn: number of carnevoirs in cell
        :param num_herb: number og herbevoirs in cell
        """

        super().__init__(row, column)
        self.food = f_ij
        self.num_herb = num_herb
        self.num_carn = num_carn


class Ocean(Map):
    """Ocean landscape """
    migratable = False
    def __init__(self, row, column):
        super().__init__(row, column)


class Mountain(Map):
    """Mountianlandscape"""
    migratable = False
    def __init__(self, row, column):
        super().__init__(row, column)


if __name__ == '__main__':
    j = Mountain(2, 3)
    print(j.row, j.column, j.migratable)
