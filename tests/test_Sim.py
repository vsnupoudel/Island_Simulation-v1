# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Cycle import Cycle

def test_food_grows():
    """ Test if food grows in Jungle and Savannah"""
    si = Cycle()
    input_map = ("""\
                    OOOO
                    OJSO
                    OOOO""")

    si.food_grows(input_map)
