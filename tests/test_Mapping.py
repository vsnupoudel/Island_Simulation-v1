# -*- coding: utf-8 -*-

"""
Geo class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from src.biosim.mapping import Savannah, Jungle, Desert, Ocean, Mountain, Cell
import pytest


class TestMapping:
    """
    Several tests for the Mapping class
    """

    @pytest.fixture()
    def Cell_obj(self):
        return Cell(2, 3)

    @pytest.fixture()
    def Mountian_obj(self):
        return Mountain(2, 3)

    @pytest.fixture()
    def Jungle_obj(self):
        return Jungle(2, 3)

    @pytest.fixture()
    def Ocean_obj(self):
        return Ocean(2, 3)

    @pytest.fixture()
    def Desert_obj(self):
        return Desert(2, 3)

    @pytest.fixture()
    def Savannah_obj(self):
        return Savannah(2, 3)

    def test_is_instance(self, Cell_obj, Mountian_obj, Jungle_obj, Ocean_obj,
                         Desert_obj, Savannah_obj):
        """Objects should be instance of class"""
        assert isinstance(Cell_obj, Cell) & isinstance(Mountian_obj, Mountain)\
               & isinstance(Jungle_obj, Jungle) & isinstance(Ocean_obj, Ocean)\
               & isinstance(Desert_obj, Desert) & \
               isinstance(Savannah_obj, Savannah), \
            "Objects should be instances of the class"

    def test_positive_input_rows_columns(self, Jungle_obj):
        """all input should be positive integers"""
        assert (Jungle_obj.row > 0) & (Jungle_obj.column > 0), \
            "All input should be positive integers"

    def test_positive_num_animals(self, Jungle_obj):
        """number of herbivores and carnivores should be a positive integer"""
        assert (Jungle_obj.n_herbs >= 0) & (Jungle_obj.n_carns >= 0), \
            "Number of animals should be positive integers"

    def test_set_and_get_function(self, Jungle_obj):
        """The set an get population methods works properly"""
        Jungle_obj.set_population({
            "loc": (2, 3),
            "pop": [{'species': 'Herbivore', 'age': 5, 'weight': 20},
                    {'species': 'Carnivore', 'age': 5, 'weight': 20}]})

        object_list = Jungle_obj.get_population()
        name_list = [type(a).__name__ for a in object_list]
        assert name_list == ["Herbivore", "Carnivore"], \
            "Not setting or getting the population properly"

    def test_sorted_herbs_and_carns(self, Jungle_obj):
        """Sorting of lists works properly"""
        Jungle_obj.set_population({
            "loc": (2, 3),
            "pop": [{'species': 'Herbivore', 'age': 5, 'weight': 30},
                    {'species': 'Herbivore', 'age': 5, 'weight': 20},
                    {'species': 'Herbivore', 'age': 5, 'weight': 10}
                    ]})

        unsorted_fitness = [h.fitness for h in Jungle_obj.herb_list]
        sorted_fitness = sorted(unsorted_fitness)

        fitness_from_herb_sorted = [h.fitness for h in Jungle_obj.herb_sorted]

        assert fitness_from_herb_sorted == sorted_fitness, "Not sorted right"
        assert [1, 2] != [2, 1]






