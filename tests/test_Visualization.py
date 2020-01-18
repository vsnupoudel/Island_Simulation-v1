# -*- coding: utf-8 -*-

"""
Tests for Animal class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"


from biosim.simulation import BioSim
from biosim.Mapping import Cell, Savannah, Jungle
from biosim.Animal import Herbivore, Carnivore
from biosim.Visualization import Visualization

import numpy as np
import pytest


class TestVisualization:
    """
    Several tests for the Visualization class
    """
    @pytest.fixture()
    def create_sim(self):
        """Creates a Simulation object"""
        map = """\
                     OOOOOOOOO
                     OSSJJSSOO
                     OOOOOOOOO
                     """

        ini_herbs = [
            {
                "loc": (2, 2),
                "pop": [
                    {"species": "Herbivore", "age": 5, "weight": 20}
                    for _ in range(200)
                ],
            }
        ]

        return BioSim(map, ini_herbs, seed=1)

    @pytest.fixture()
    def create_vis(self, create_sim):
        """Creates a Visualization object"""
        return Visualization(create_sim.object_matrix)

    def test_set_graphics(self, create_vis):
        """tests subplots of set_graphics"""
        create_vis._set_graphics(5)
        assert create_vis._fig is not None
        assert create_vis._map_ax is not None
        assert create_vis._herb_line is not None
        assert create_vis._carn_line is not None
        assert create_vis._herb_ax is not None
        assert create_vis._carn_ax is not None

    def test_create_map(self, create_vis, create_sim):
        """Map should be created"""
        create_vis._set_graphics(5)
        create_vis.create_map(create_sim.island_matrix)
        assert create_vis._img_axis is not None

    def test_update_herb_ax(self, create_vis, create_sim):
        """map of herbivores should be created"""
        create_vis._set_graphics(5)
        ax_1 = create_vis._herb_axis
        create_vis.update_herb_ax(create_sim.herbivore_distribution)
        ax_2 = create_vis._herb_axis

        assert create_vis._herb_axis is not None
        assert ax_1 != ax_2

    def test_update_carn_ax(self, create_vis, create_sim):
        """map of carnivores should be created"""
        create_vis._set_graphics(5)
        ax_1 = create_vis._carn_axis
        create_vis.update_carn_ax(create_sim.carnivore_distribution)
        ax_2 = create_vis._carn_axis

        assert create_vis._carn_axis is not None
        assert ax_1 != ax_2

    def test_update_mean_ax(self):
        """herbivore and carnivore line should be created"""
        pass

    def test_make_movie(self):
        """makes movie"""
        pass






