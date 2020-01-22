# -*- coding: utf-8 -*-

"""
Tests for the mapping file
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from src.biosim.terrain import Savannah, Jungle, Desert, Ocean, Mountain, Cell
import pytest


class TestMapping:
    """
    Several tests for the Mapping class
    """

    @pytest.fixture()
    def cell_obj(self):
        return Cell(2, 3)

    @pytest.fixture()
    def mountian_obj(self):
        return Mountain(2, 3)

    @pytest.fixture()
    def jungle_obj(self):
        return Jungle(2, 3)

    @pytest.fixture()
    def ocean_obj(self):
        return Ocean(2, 3)

    @pytest.fixture()
    def desert_obj(self):
        return Desert(2, 3)

    @pytest.fixture()
    def savannah_obj(self):
        return Savannah(2, 3)

    def test_is_instance(self, cell_obj, mountian_obj, jungle_obj, ocean_obj,
                         desert_obj, savannah_obj):
        """Objects should be instance of class"""
        assert isinstance(cell_obj, Cell) & isinstance(mountian_obj, Mountain)\
            & isinstance(jungle_obj, Jungle) & isinstance(ocean_obj, Ocean)\
            & isinstance(desert_obj, Desert) & \
            isinstance(savannah_obj, Savannah), \
            "Objects should be instances of the class"

    def test_positive_input_rows_columns(self, jungle_obj):
        """all input should be positive integers"""
        assert (jungle_obj.row > 0) & (jungle_obj.column > 0), \
            "All input should be positive integers"

    def test_positive_num_animals(self, jungle_obj):
        """number of herbivores and carnivores should be a positive integer"""
        assert (jungle_obj.n_herbs >= 0) & (jungle_obj.n_carns >= 0), \
            "Number of animals should be positive integers"

    def test_set_and_get_function(self, jungle_obj):
        """The set an get population methods works properly"""
        jungle_obj.set_population({
            "loc": (2, 3),
            "pop": [{'species': 'Herbivore', 'age': 5, 'weight': 20},
                    {'species': 'Carnivore', 'age': 5, 'weight': 20}]})

        object_list = jungle_obj.get_population()
        name_list = [type(a).__name__ for a in object_list]
        assert name_list == ["Herbivore", "Carnivore"], \
            "Not setting or getting the population properly"

    def test_sorted_herbs_and_carns(self, jungle_obj):
        """Sorting of lists works properly"""
        jungle_obj.set_population({
            "loc": (2, 3),
            "pop": [{'species': 'Herbivore', 'age': 5, 'weight': 30},
                    {'species': 'Herbivore', 'age': 5, 'weight': 20},
                    {'species': 'Herbivore', 'age': 5, 'weight': 10}
                    ]})

        unsorted_fitness = [h.fitness for h in jungle_obj.herb_list]
        sorted_fitness = sorted(unsorted_fitness)

        fitness_from_herb_sorted = [h.fitness for h in jungle_obj.herb_sorted]

        assert fitness_from_herb_sorted == sorted_fitness, "Not sorted right"
        assert [1, 2] != [2, 1]
