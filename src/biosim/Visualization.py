# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import numpy as np
import os
import matplotlib.pyplot as plt

class Visualization:
    """
    Plotting island map, heatmaps of herbivore and carnivore distribution
    and line graph of herbivore and carnivore count.

    :ivar _fig:             plt.figure(default, None), figure to put subplots in
    :ivar _map_ax:          (default, None) plot of the island map
    :ivar _img_axis:        (default, None) axis to _map_ax
    :ivar _herb_ax:         heatmap(default, None), plot for herbivore
                                         distribution
    :ivar _carn_ax:         heatmap(default, None), plot for carnivore
                                         distribution
    :ivar _mean_ax:         (default, None) plot for the linegraphs
    :ivar _herb_line:       (default, None) herbivore-count line in _mean_ax
    :ivar _carn_line:       (default, None) carnivore-count line in _mean_ax
    :ivar _herb_axis:       (default, None) axis to _herb_ax
    :ivar _carn_axis:       (default, None) axis to _carn_ax

    """


    def __init__(self):
        self._step = 0
        # the following will be initialized by _setup_graphics
        self._fig = None
        self._map_ax = None
        self._img_axis = None
        self._mean_ax = None
        self._herb_ax = None
        self._carn_ax = None
        self._herb_axis = None
        self._carn_axis = None

        self._herb_line = None
        self._carn_line = None

    def set_graphics(self, y_lim, x_lim):
        """
        Sets up the graphics with 4 subplots

        :param y_lim:       float, y limit of plot
        :param x_lim:       int, x limit of plot
        :return: None
        """
        # create new figure window
        if self._fig is None:
            self._fig = plt.figure(figsize=(8,8))
            plt.title("Maximum number of years: "+str(x_lim), loc='left')
            plt.axis('off')

        if self._map_ax is None:
            self._map_ax = self._fig.add_subplot(2, 2, 1)
            self._img_axis = None

        if self._herb_ax is None:
            self._herb_ax = self._fig.add_subplot(2, 2, 2)
            self._herb_axis = None

        if self._carn_ax is None:
            self._carn_ax = self._fig.add_subplot(2, 2, 3)
            self._carn_axis = None

        if self._mean_ax is None:
           self._mean_ax = self._fig.add_subplot(2, 2, 4)
           self._mean_ax.set_ylim(0, y_lim)
           self._mean_ax.set_xlim(0, x_lim)


        if self._herb_line is None:
            herb_plot = self._mean_ax.plot(np.arange(0, x_lim),
                                           np.full(x_lim, np.nan))
            self._herb_line = herb_plot[0]

        # Do the same for carn_line
        if self._carn_line is None:
            carn_plot = self._mean_ax.plot(np.arange(0, x_lim),
                                           np.full(x_lim, np.nan))
            self._carn_line = carn_plot[0]


    def create_map(self, data):
        """
        Creates island map. Called one time at the start of the simuation.

        :param data:    array, 2D array of map spesifications
        :return: None
        """
        self._img_axis = self._map_ax.imshow(data, cmap='terrain'
                                             , vmax=20, vmin=1)

    def update_herb_ax(self, herb_data, herb_limit):
        """
        Updates heatmap for herbivore distribution

        :param herb_data:   array, 2D array with number of herbivores in each
                            cell
        :param vmax:        int, upper limit for colourbar
        :return: None
        """
        if self._herb_axis is not None:
            self._herb_axis.set_data(herb_data)
        else:
            self._herb_axis = self._herb_ax.imshow(herb_data,
                                                 interpolation='nearest',
                                                 cmap="Greens", vmin =0,
                                                   vmax= herb_limit)
            self._herb_ax.figure.colorbar(self._herb_axis, ax=self._herb_ax
                                          , orientation='horizontal')

    def update_carn_ax(self, carn_data, carn_limit):
        """
        Updates heatmap for carnivore distribution

        :param carn_data:    array, 2D array with number of carnivores in each
                             cell
        :param vmax:         int, upper limit for colourbar
        :return: None
        """
        if self._carn_axis is not None:
            self._carn_axis.set_data(carn_data)
        else:
            self._carn_axis = self._carn_ax.imshow(carn_data,
                                                 interpolation='nearest',
                                                 cmap="OrRd", vmin =0,
                                                   vmax= carn_limit)
            self._carn_ax.figure.colorbar(self._carn_axis, ax=self._carn_ax
                                          , orientation='horizontal'
                                          )

    def update_mean_ax(self, herb_num, carn_num):
        """
        Updates linegraphs for herbivore and carnivore count

        :param herb_num:    int, total number of herbivores on island
        :param carn_num:    int, total number of carnivores on island
        :return: None
        """
        ydata = self._herb_line.get_ydata()
        ydata[self._step] = herb_num
        self._herb_line.set_ydata(ydata)
        # Another line for carnivore
        ydata = self._carn_line.get_ydata()
        ydata[self._step] = carn_num
        self._carn_line.set_ydata(ydata)
        self._step += 1

    def update_graphics(self, herb_pos, carn_pos, num_animals_per_sp,
                        col_limits):
        """
        Updates graphics with current data

        :param col_limits: limits of colourbars for herbivores and carnivores
                           in a dictionary format
        :param herb_pos:     array, 2D array containing herbivore distribution
                             on the island
        :param carn_pos:     array, 2D array containing carnivore distribution
                             on the island
        :param num_animals:  number of herbivores and carnivores
        :return: None
        """
        # create_map will be called separately
        herb_limit = col_limits['Herbivore']
        carn_limit = col_limits['Carnivore']
        self.update_herb_ax(herb_pos, herb_limit)
        self.update_carn_ax(carn_pos, carn_limit)
        self.update_mean_ax(num_animals_per_sp["Herbivore"],
                            num_animals_per_sp["Carnivore"])
        plt.pause(1e-9)
