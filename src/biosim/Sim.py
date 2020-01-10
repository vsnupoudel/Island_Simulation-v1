# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo
from biosim.Mapping import Jungle, Savannah

class Simulation:
    def __init__(self):
        pass

    def food_grows(self, input_map):

        for row in input_map:
            for col in input_map:

                cell = input_map[row][col]
                if cell == Savannah:
                    cell.f_ij += cell.alpha * (cell.f_max - cell.f_ij)
                elif cell == Jungle:
                    cell.f_ij = cell.f_max


