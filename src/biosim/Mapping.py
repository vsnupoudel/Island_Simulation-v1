# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import ...


class Map:
    def __init__(self, row, column):
        self.row = row
        self.column = column


class Sav(Map):
    f_max = 300

    def __init__(self, f_ij=300, alpha=0.3, row, column, num_carn,
                 num_herb):
        """
        parameters
        """
        self.food = f_ij
        self.aplha = alpha
        self.num_carn = num_carn
        self.num_herb = num_herb

        super().__init__()


class Jungle(Map):
    f_max = 800

    def __int__(self, f_ij=f_max, row, column, num_carn, num_herb):
        """
        Parameters
        """
        self.food = f_ij
        self.num_carn = num_carn
        self.num_herb = num_herb

        super().__init__()


class Desert(Map):
    f_max = 0

    def __init__(self, f_ij=f_max, row, column, num_carn, num_herb):
        """
        Parameters
        """
        self.food = f_ij
        self.num_herb = num_herb
        self.carn = num_carn

        super().__init__()


class Ocean(Map):
    def __init__(self, row, column):
        super().__init__()


class Mountian(Map):
    def __init__(self, row, column):
        super().__init__()


