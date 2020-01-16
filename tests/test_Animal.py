# -*- coding: utf-8 -*-

"""
Tests for Animal class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Animal import Animal, Herbivore, Carnivore


def test_animal_not_dead():
    """ New animal should not be dead"""
    h = Herbivore(2, 10)
    c = Carnivore(2, 10)
    assert h.is_dead == False
    assert c.is_dead == False

def test_positive_input():
    """age and weight should be positive"""
    h = Herbivore(2, 10)
    c = Carnivore(2, 10)
    assert h.age > 0 and (h.weight > 0)
    assert c.age > 0 and (c.weight > 0)

def test_positive_fitness():
    """Animal should have positive fitness"""
    h = Herbivore(2, 10)
    c = Carnivore(2, 10)
    assert h.fitness > 0
    assert c.fitness > 0




