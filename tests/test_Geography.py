# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim import Geo

class testGeo:
    """ Tests for Geo class"""

    def test_proper_letters(self):
        """all letters should either be: = O, M, J, S, D"""
        with pytest.raises(ValueError):
            Geo("yyyy")


    def test_same_legth(self):
        """rows have same length"""
        with pytest.raises(ValueError):
            Geo(""""\OOOOOOO
            JJJJJ""")





