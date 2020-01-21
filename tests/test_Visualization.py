# -*- coding: utf-8 -*-

"""
Tests for Visualization class
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"


from src.biosim.simulation import BioSim
from src.biosim.visualization import Visualization

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
        return Visualization()

    def test_set_graphics(self, create_vis):
        """tests subplots of set_graphics"""
        create_vis.set_graphics(100, 20)
        assert create_vis._fig is not None, "Figure should not be None"
        assert create_vis._map_ax is not None, "Figure should not be None"
        assert create_vis._herb_line is not None, "Figure should not be None"
        assert create_vis._carn_line is not None, "Figure should not be None"
        assert create_vis._herb_ax is not None, "Figure should not be None"
        assert create_vis._carn_ax is not None, "Figure should not be None"

    def test_create_map(self, create_vis, create_sim):
        """Map should be created"""
        create_vis.set_graphics(100, 20)
        create_vis.create_map(create_sim.island_matrix)
        assert create_vis._img_axis is not None, "Figure should not be None"

    def test_update_herb_ax(self, create_vis, create_sim):
        """map of herbivores should be created"""
        create_vis.set_graphics(100, 20)
        ax_1 = create_vis._herb_axis
        create_vis.update_herb_ax(create_sim.herbivore_distribution, 20)
        ax_2 = create_vis._herb_axis

        assert create_vis._herb_axis is not None, "Figure should not be None"
        assert ax_1 != ax_2, "axis should not be equal"

    def test_update_carn_ax(self, create_vis, create_sim):
        """map of carnivores should be created"""
        create_vis.set_graphics(100, 20)
        ax_1 = create_vis._carn_axis
        create_vis.update_carn_ax(create_sim.carnivore_distribution, 20)
        ax_2 = create_vis._carn_axis

        assert create_vis._carn_axis is not None, "Figure should not be None"
        assert ax_1 != ax_2, "axis should not be equal"

    def test_update_mean_ax(self):
        """herbivore and carnivore line should be created"""
        pass

    def test_make_movie(self):
        """makes movie"""
        pass
