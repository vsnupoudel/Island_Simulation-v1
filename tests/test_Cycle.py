# -*- coding: utf-8 -*-

"""
Test for Cycle class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from cycle import Cycle
from simulation import BioSim
from pytest_mock import mocker
import pytest
import numpy

class TestCycle:
    """
    Several tests for the Cycle class
    """


    @pytest.fixture()
    def input_map(self):
        """Makes an empty map"""
        map = ("""\
                        OOOO
                        OJSO
                        OOOO""")
        return map


    @pytest.fixture()
    def ini_pop(self):
        """Defines initial population"""
        herbs = [
                        {
                            "loc": (1, 1),
                            "pop": [
                                {"species": "Herbivore", "age": 5, "weight": 50}
                                for _ in range(120)
                            ]
                        }
                    ] + [
                        {
                            "loc": (1, 1),
                            "pop": [
                                {"species": "Carnivore", "age": 5, "weight": 50}
                                for _ in range(20)
                            ]
                        }
                    ]
        return herbs

    @pytest.fixture()
    def create_s(self, input_map, ini_pop):
        """Creates a Simulation object"""
        s = BioSim(input_map, ini_pop, seed=1)
        return s


    @pytest.fixture()
    def create_c(self, input_map, ini_pop, create_s):
        """Creates a Cycle object"""
        c = Cycle(create_s.object_matrix)
        return c


    def test_get_adjacent_migratable_cells(self, create_c):
        """should only get migratable cells"""
        migratable_cells  = [type(cell).__name__ for cell in
                           create_c.get_adjacent_migratable_cells(1, 1)]
        assert migratable_cells == ['Savannah'], \
            "Should onnly get migratable cells"


    def test_food_grows_Savannah(self, create_c):
        """Food amount in each Savannah cell should increase"""
        prev_food_sav = create_c.object_matrix[1][2].f_ij
        create_c.food_grows()
        assert create_c.object_matrix[1][2].f_ij > prev_food_sav, \
            "Food amount should increase"


    def test_max_food_Jungle(self, create_c):
        """When food grows in Jungle cells it should be set to f_max = 800"""

        prev_food_jun = create_c.object_matrix[1][1].f_ij
        create_c.food_grows()
        assert create_c.object_matrix[1][1].f_ij >= prev_food_jun
        assert create_c.object_matrix[1][1].f_ij == create_c.object_matrix[1][1].parameters[
            'f_max'], "f_ij should be equal to f_max when food grows in Jungle"


    def test_fitness_increase_after_feeding(self, create_c):
        """The animals fitness should increase after feeding"""
        prev_fitness_array = [ a.fitness for a in create_c.object_matrix[1][
            1].animal_object_list ]
        create_c.food_grows()
        create_c.animals_eat()
        curr_fitness_array = [a.fitness for a in create_c.object_matrix[1][
            1].animal_object_list]
        # cached property was not working in fitness, so removed it
        assert curr_fitness_array > prev_fitness_array, \
            "Animals fitness should increase after feeding"


    def test_animals_reproduce(self, input_map, ini_pop):
        """Animals should reproduce properly"""
        s = BioSim(input_map, ini_pop, seed=1)
        herb_count_prev = s.object_matrix[1][1].n_herbs
        carn_count_prev = s.object_matrix[1][1].n_carns

        c = Cycle(s.object_matrix)
        c.food_grows()
        c.animals_reproduce()
        herb_count_curr = s.object_matrix[1][1].n_herbs
        carn_count_curr = s.object_matrix[1][1].n_carns

        assert carn_count_curr > carn_count_prev, "Animals have not reproduced"
        assert herb_count_curr > herb_count_prev, "Animals have not reproduced"


    def test_animals_migrate(self, mocker, create_c, create_s):
        """Animals should migrate properly"""
        mocker.patch('numpy.random.random', return_value=0)
        create_c.animals_migrate()
        assert len(create_s.object_matrix[1][1].animal_object_list) == 0,\
            "Animals did not migrate"
        assert len(create_s.object_matrix[1][2].animal_object_list) == 140, \
            "Animals did not migrate"


    def test_animals_dont_migrate(self, mocker, create_c, create_s):
        """Tests if animals do not migrate"""
        mocker.patch('numpy.random.random', return_value=1)
        create_c.animals_migrate()
        assert len(create_s.object_matrix[1][1].animal_object_list) == 140, \
            "Animals did migrate"
        assert len(create_s.object_matrix[1][2].animal_object_list) == 0, \
            "Animals did migrate"


    def test_animals_migrate(self, create_c, create_s):
        """Animals should migrate properly"""
        create_c.animals_migrate()
        assert len(create_s.object_matrix[1][1].animal_object_list) > 0, \
            "Animals did not migrate"
        assert len(create_s.object_matrix[1][1].animal_object_list) < 140, \
            "Animals did not migrate"
        assert len(create_s.object_matrix[1][2].animal_object_list) > 0, \
            "Animals did not migrate"
        assert len(create_s.object_matrix[1][2].animal_object_list) < 140, \
            "Animals did not migrate"


    def test_all_animals_die(self, mocker, create_c, create_s ):
        """All animals should die"""
        mocker.patch('numpy.random.random', return_value=0)
        create_c.animals_die()
        assert create_s.object_matrix[1][1].animal_object_list == [], \
            "All animals did not die"


    def test_no_animals_die(self, mocker, create_c, create_s):
        "No animals should die"
        mocker.patch('numpy.random.random', return_value=1)
        old_list = create_s.object_matrix[1][1].animal_object_list
        create_c.animals_die()
        assert create_s.object_matrix[1][1].animal_object_list == old_list, \
            "Some animals died"


    def test_death_probability(self, mocker, create_c, create_s):
        """Check that death probability works properly"""
        mocker.patch('numpy.random.random', return_value=0.001)
        obj_id = id( create_s.object_matrix[1][1].animal_object_list[0] )
        death_prob = create_s.object_matrix[1][1].animal_object_list[0].death_prob
        create_c.animals_die()
        list_id = [id(a) for a in create_s.object_matrix[1][1].animal_object_list]
        if numpy.random.random() < death_prob:
            assert obj_id not in list_id, \
                "Object ID should not exist after animals die"
        else:
            assert obj_id in list_id, \
                "Object ID should exist if animals do not die"
