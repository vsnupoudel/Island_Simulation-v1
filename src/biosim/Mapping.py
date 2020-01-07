# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import ...


class Map:
    def __init__(self, row, column):
        """
        :param row: row index
        :param column: column index
        """
        self.row = row
        self.column = column


class Savannah(Map):
    f_max = 300
    migratable = True
    """Savannah landscape"""

    def __init__(self, f_ij=300, alpha=0.3, num_carn,
                 num_herb):
        """
        :param f_ij: food in cell
        :param alpha: calculation parameter
        :param num_carn: number of carnevoirs in cell
        :param num_herb: number og herbevoirs in cell
        """
        self.food = f_ij
        self.aplha = alpha
        self.num_carn = num_carn
        self.num_herb = num_herb

        super().__init__()


class Jungle(Map):
    f_max = 800
    migratable = True
    """Jungle landscape"""

    def __int__(self, f_ij=f_max, num_carn, num_herb):
        """
        :param f_ij: food in cell
        :param num_carn: number of carnevoirs in cell
        :param num_herb: number og herbevoirs in cell
        """
        self.food = f_ij
        self.num_carn = num_carn
        self.num_herb = num_herb

        super().__init__()


class Desert(Map):
    """Desert landscape"""
    migratable = True
    f_max = 0

    def __init__(self, f_ij=f_max, num_carn, num_herb):
        """"
        :param f_ij: food in cell
        :param num_carn: number of carnevoirs in cell
        :param num_herb: number og herbevoirs in cell
        """
        self.food = f_ij
        self.num_herb = num_herb
        self.carn = num_carn

        super().__init__()


class Ocean(Map):
    """Ocean landscape """
    migratable = False

    def __init__(self, row, column):
        super().__init__()


class Mountian(Map):
    """Mountianlandscape"""
    migratable = False

    def __init__(self, row, column):
        super().__init__()


