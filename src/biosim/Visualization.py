# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Herbivore_simulation import HSimulation
from biosim.Geography import Geo
import seaborn as sns
import numpy as np

import matplotlib.pyplot as plt

class Visualization:
    """
    Plotting island map , heatmaps and line graph
    """

    def show(self):
        plt.show()
    def __init__(self, object_matrix):
        """
        :param object_matrix: 2D array of cell objects containing herbivores
        and carnivores
        """
        self.object_matrix = object_matrix           #system

        self._step = 0
        self._final_step = 20
        self._img_ctr = 0


        # the following will be initialized by _setup_graphics
        self._fig = None
        self._map_ax = None
        self._img_axis = None
        self._mean_ax = None
        self._mean_line = None
        self._herb_ax = None
        self._carn_ax = None
        self._herb_axis = None
        self._carn_axis = None

    def simulate(self, num_steps, vis_steps=1, img_steps=None):
        """
        Simulates prosess
        :param num_steps:
        :param vis_steps:
        :param img_steps:
        :return:
        """


    def _set_graphics(self):
        """
        sets the graphics
        :return:
        """

        # create new figure window
        if self._fig is None:
            self._fig = plt.figure()

        if self._map_ax is None:
            self._map_ax = self._fig.add_subplot(2, 2, 1)
            self._img_axis = None

        if self._herb_ax is None:
            self._herb_ax = self._fig.add_subplot(2, 2, 2)
            self._herb_axis = None                                #herb_axes?

        if self._carn_ax is None:
            self._carn_ax = self._fig.add_subplot(2, 2, 3)
            self._carn_axis = None

        if self._mean_ax is None:                                #linegraph
           self._mean_ax = self._fig.add_subplot(2, 2, 4)
           self._mean_ax.set_ylim(0, 50)

        # needs updating on subsequent calls to simulate()
        self._mean_ax.set_xlim(0, self._final_step + 1)

        if self._mean_line is None:
            mean_plot = self._mean_ax.plot(np.arange(0, self._final_step),   #x, y
                                           np.full(self._final_step, np.nan))
            self._mean_line = mean_plot[0]
        else:
            xdata, ydata = self._mean_line.get_data()
            xnew = np.arange(xdata[-1] + 1, self._final_step)
            if len(xnew) > 0:
                ynew = np.full(xnew.shape, np.nan)
                self._mean_line.set_data(np.hstack((xdata, xnew)),
                                         np.hstack((ydata, ynew)))


    def update_map(self, data):
        """
        Updates map
        :return:
        """
        if self._img_axis is not None:
            self._img_axis.set_data(data)
        else:
            # self._img_axis = self._map_ax.imshow(data,
            #                                      interpolation='nearest',
            #                                      vmin=0, vmax=1)
            self._img_axis = self._map_ax.imshow(data, cmap='terrain'
                                                 , vmax=20, vmin=1)

            plt.colorbar(self._img_axis, ax=self._map_ax,
                         orientation='horizontal')


    def update_herb_ax(self, herb_data):
        """
        Updates herb_ax
        :return:
        """
        if self._herb_axis is not None:
            self._herb_axis.set_data(herb_data)

        else:
            self._herb_axis = sns.heatmap(herb_data, linewidth=0.5,
                                         cmap="Greens", ax=self._herb_ax)
#        plt.show()

    def update_carn_ax(self, carn_data):
        """
    Updates carn_ax
        :return:
        """
        if self._carn_axis is not None:
            self._carn_axis.set_data(carn_data)

        else:
            self._carn_axis = sns.heatmap(carn_data, linewidth=0.5,
                                         cmap="OrRd", ax=self._carn_ax)


    def update_mean_ax(self, mean):
        ydata = self._mean_line.get_ydata()
        ydata[self._step] = mean
        self._mean_line.set_ydata(ydata)
        self._step += 1
        # plt.show()

    def update_graphics(self, herb_pos, carn_pos, num_herbs):
        """
        Updates graphics with current data
        :return:
        """
        self.update_map(self.object_matrix)
        self.update_herb_ax(herb_pos)
        self.update_carn_ax(carn_pos)
        self.update_mean_ax(num_herbs)

        plt.pause(1e-6)


    def save_graphics(self):
        """
        Saves graphics
        :return:
        """
        if self._image_base is None:
            return

        plt.savefig('{base}_{num:05d}.{type}'.format(base=self._img_base,
                                                     num=self._img_ctr,
                                                     type=self._img_fmt))
        self._img_ctr += 1




    def plot_all(self):
        row_num = np.shape(self.object_matrix)[0]  # g.geo_shape[0]
        column_num = np.shape(self.object_matrix)[1]
        total_cells = row_num * column_num

        print(row_num, column_num, total_cells)

        # plt.subplots_adjust(wspace=0, hspace=0)

        # Herbivore heatmap
        h_matrix = np.zeros((row_num, column_num))
        c_matrix = np.zeros((row_num, column_num))

        for row, list_of_obj in enumerate(self.object_matrix):
            for col, cell in enumerate(list_of_obj):
                for animal in cell.animal_object_list:
                    if type(animal).__name__ == "Herbivore":
                        h_matrix[row][col] += 1
                    else:
                        c_matrix[row][col] += 1

        # print(h_matrix )
        # print(c_matrix)

        fig = plt.figure()
        ax = fig.add_subplot(223)
        ax = sns.heatmap(h_matrix, linewidth=0.5, cmap="Greens")
        ax = fig.add_subplot(224)
        ax = sns.heatmap(h_matrix, linewidth=0.5, cmap="OrRd")

        # For the map of the island
        color_dict = {"Ocean": 2, "Desert": 11, "Savannah": 8,
                      "Jungle": 6, "Mountain": 16}

        island_matrix = np.zeros((row_num, column_num))

        for row, list_of_obj in enumerate(self.object_matrix):
            for col, cell in enumerate(list_of_obj):
                island_matrix[row][col] = color_dict[type(cell).__name__]
        # print(island_matrix)

        ax = fig.add_subplot(221)
        ax = plt.imshow(island_matrix, cmap='terrain', vmax=20, vmin=1)

        # For line plot
        h_count = 0
        c_count = 0
        h_count_list = []
        c_count_list = []

        for row, list_of_obj in enumerate(self.object_matrix):
            for col, cell in enumerate(list_of_obj):
                for animal in cell.animal_object_list:
                    if type(animal).__name__ == "Herbivore":
                        h_count += 1
                    else:
                        c_count += 1

        h_count_list.append(h_count)
        c_count_list.append(c_count)
        print(h_count_list, c_count_list)

        ax = fig.add_subplot(222)
        ax = plt.plot(h_count_list)
        ax = plt.plot(c_count_list)

        plt.show()

