# -*- coding: utf-8 -*-

__author__ = "Anders Huse"
__email__ = "huse.anders@gmail.com"

from Cycle import Cycle
from Geography import Geo
from Visualization import Visualization
from Mapping import Savannah, Jungle
from Animal import Herbivore, Carnivore

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import subprocess


class BioSim:
    """
    Initialize and execute simulation. This class takes in map and population,
    and converts them to objects.

    :ivar island_map:      str, Multi-line string specifying island geography
    :ivar ini_pop:         list, List of dictionaries specifying initial
                           population
    :ivar seed:            int(default, 1), random number seed
    :ivar ymax_animals:    int(default, 10000), Number specifying y-axis limit
                           for graph showing animal numbers
    :ivar cmax_animals:    dict(default, None), Dictionary specifying
                           color-code limits for animal densities
    :ivar total_years:     int(default, 60), total number of years for all the
                           sub-simulations
    :ivar img_base:
    :ivar img_fmt:         str(default, png), image fmt

    :ivar num_images:      int(default, 0), number of images
    :ivar object_matrix:   array, 2D array of cell objects containing
                           herbivores and carnivores

    :ivar v:                Instance of Visualization class
    :ivar v.set_graphics:   Graphics are set

    """

    def __init__(
            self,
            island_map,
            ini_pop,
            seed=1,
            ymax_animals=10000,  # logic to be added when this is none
            cmax_animals=None,
            total_years=60,
            img_base=None,
            img_fmt="png"
    ):
        """
        :param island_map: Multi-line string specifying island geography
        :param ini_pop: List of dictionaries specifying initial population
        :param seed: Integer used as random number seed
        :param ymax_animals: Number specifying y-axis limit for graph
        showing animal numbers
        :param cmax_animals: Dict specifying color-code limits for animal
        densities
        :param total_years: total number of years for all the sub-simulations
        default number is 60
        :param img_base: Path relative to the code being run, where the user
        intends to store the images. If is none, no image is stored
        :param img_fmt: String with file type for figures, e.g. 'png'

        total_years should be greater than the sum of individual years of
        simulations.

        If ymax_animals is None, the y-axis limit should be adjusted
        automatically.
        If cmax_animals is None, sensible, fixed default values should be used.
        cmax_animals is a dict mapping species names to numbers, e.g.,
           {'Herbivore': 50, 'Carnivore': 20}

        If img_base is None, no figures are written to file.
        Filenames are formed as

            '{}\\_{:05d}.{}'.format(img_base, img_no, img_fmt)

        where img_no are consecutive image numbers starting from 0.
        img_base should contain a path and beginning of a file name.
        """
        self.num_images = 0
        self.current_year = 0
        self.seed = seed
        self.ini_pop = ini_pop
        self.island_map = Geo(island_map)
        self.object_matrix = self.island_map.object_matrix
        self.ymax_animals = ymax_animals
        self.total_years = total_years
        self.img_fmt = img_fmt
        self.img_base = img_base

        # Set the population in respective cell in the matrix
        for one_location_list in self.ini_pop:
            x, y = one_location_list['loc'][0], one_location_list['loc'][1]
            self.object_matrix[x][y].set_population(one_location_list)

        self.v = Visualization(self.object_matrix)
        self.v.set_graphics(self.ymax_animals, self.total_years)

    def set_animal_parameters(self, species, params):
        """
        Set parameters for animal species.

        :param species:  string, name of animal species
        :param params:   dict, valid parameter specification for species
        """
        if species == 'Herbivore':
            Herbivore.up_par(params)
        else:
            Carnivore.up_par(params)

    def set_landscape_parameters(self, landscape, params):
        """
        Set parameters for landscape type.

        :param landscape:   string, code letter for landscape
        :param params:      dict, parameter specification for landscape
        """
        if landscape == 'S':
            Savannah.parameters.update(params)
        else:
            Jungle.parameters.update(params)

    def simulate(self, num_years=20, vis_years=1, img_years=1,
                 colorbar_limits=None):
        """
        Runs simulation while visualizing the result.
        This method will:

        - Make a Images directory if it does not exist
        - Make a Visualization object to plot the initial state of the
          map and population
        - Create the first plot which is the map of the island
        - Update the remaining three plots among the subplots, which contain
          Herbivore and Carnivore distribution and line graphs of herbivore
          and carnivore count
        - Save the figure as an image (png)
        - Execute the cycle in fixed order and then update graphics and number
          of steps (years)
        - At last, make movie out of the pictures stored

        Image files will be numbered consecutively.

        :param num_years:     int, number of years to simulate, default
                              number is 20
        :param vis_years:     int, years between visualization updates
        :param img_years:     int(default: None), years between visualizations
                              saved to files
        :param y_lim:         float, y axis limit of the line graph
        :param colorbar_limits:  dict, vmax for the colorbars for herbivores
                                  and carnivores
        """
        if colorbar_limits is None:
            colorbar_limits = {"Herbivore": 200, "Carnivore": 200}

        self.v.create_map(self.island_matrix)

        step = 0
        self.v.update_graphics(self.herbivore_distribution,
                               self.carnivore_distribution,
                               self.num_animals_per_species
                               , colorbar_limits)
        if self.img_base:
            if not os.path.exists(self.img_base):
                os.makedirs(self.img_base)
            plt.savefig('{}\\_{:05d}.{}'.format(self.img_base, self.num_images,
                                                self.img_fmt))

        # plt.savefig('Images\\Image-{0:03d}.png'.format(self.num_images))

        c = Cycle(self.object_matrix)
        while step <= num_years:
            c.food_grows()
            c.animals_eat()
            c.animals_reproduce()
            c.animals_migrate()
            c.animals_die()
            c.animals_age()
            self.v.update_graphics(self.herbivore_distribution,
                                   self.carnivore_distribution,
                                   self.num_animals_per_species,
                                   colorbar_limits)

            step += 1
            self.current_year += 1

            if (step % img_years == 0) & (self.img_base is not None):
                plt.savefig('{}\\_{:05d}.{}'.format(self.img_base
                                                    , self.num_images,
                                                    self.img_fmt))

                self.num_images += 1

        self.current_year = self.current_year - 1

    def add_population(self, population):
        """
        Add a population to the island

        :param population:  list, List of dictionaries specifying population
        """
        for one_location_list in population:
            x, y = one_location_list['loc'][0], one_location_list['loc'][1]
            self.object_matrix[x][y].set_population(one_location_list)

    @property
    def year(self):
        """
        :return: year    int, current year on island
        """
        return self.current_year

    @property
    def num_animals_per_species(self):
        """
        Total number of herbivores and carnivores on island

        :return: animals_count_dict  dict, dictionary containing number of
                                     herbivores and carnivores on island
        """
        h_count = 0
        c_count = 0
        animal_count_dict = {"Herbivore": 0, "Carnivore": 0}

        for row, list_of_obj in enumerate(self.object_matrix):
            for col, cell in enumerate(list_of_obj):
                for animal in cell.animal_object_list:
                    if type(animal).__name__ == "Herbivore":
                        animal_count_dict['Herbivore'] += 1
                    else:
                        animal_count_dict['Carnivore'] += 1

        return animal_count_dict

    @property
    def num_animals(self):
        return (self.num_animals_per_species['Herbivore'] +
                self.num_animals_per_species['Carnivore'])

    @property
    def herbivore_distribution(self):
        """Pandas DataFrame with herbivore count for each cell on island."""  # not dataframe
        row_num = np.shape(self.object_matrix)[0]
        column_num = np.shape(self.object_matrix)[1]

        h_matrix = np.zeros((row_num, column_num))

        for row, list_of_obj in enumerate(self.object_matrix):
            for col, cell in enumerate(list_of_obj):
                for animal in cell.animal_object_list:
                    if type(animal).__name__ == "Herbivore":
                        h_matrix[row][col] += 1

        return h_matrix

    @property
    def carnivore_distribution(self):
        """Pandas 2D matrix with carnivore count for each cell on island."""
        row_num = np.shape(self.object_matrix)[0]
        column_num = np.shape(self.object_matrix)[1]

        c_matrix = np.zeros((row_num, column_num))

        for row, list_of_obj in enumerate(self.object_matrix):
            for col, cell in enumerate(list_of_obj):
                for animal in cell.animal_object_list:
                    if type(animal).__name__ == "Carnivore":
                        c_matrix[row][col] += 1

        return c_matrix

    @property
    def animal_distribution(self):
        """Pandas DataFrame with animal count for each cell on island."""

        cord_list = []
        herb_list = []
        carn_list = []
        for row in self.object_matrix:
            for el in row:
                cord_list.append((el.row, el.column))
                herb_list.append(el.n_herbs)
                carn_list.append(el.n_carns)

        ani_dist = pd.DataFrame(cord_list)
        ani_dist['Herbivores'] = herb_list
        ani_dist['Carnivores'] = carn_list
        # print(ani_dist)
        return ani_dist

    @property
    def island_matrix(self):
        """
        Creates a color map according to the type of landscape in each cell.
        """
        color_dict = {"Ocean": 2, "Desert": 11, "Savannah": 8,
                      "Jungle": 6, "Mountain": 16}
        row_num = np.shape(self.object_matrix)[0]
        column_num = np.shape(self.object_matrix)[1]

        island_matrix = np.zeros((row_num, column_num))

        for row, list_of_obj in enumerate(self.object_matrix):
            for col, cell in enumerate(list_of_obj):
                island_matrix[row][col] = color_dict[type(cell).__name__]

        return island_matrix

    def make_movie(self):
        """Makes a movie of a series of images"""
        # Input_image_path = '{}_{:05d}.{}'.format(self.img_base,
        #                                          self.img_number,
        #                                          self.img_fmt)
        subprocess.run(['ffmpeg',
                        '-f', 'image2',
                        '-r', '3',
                        '-i', 'Images\\_%05d.png',
                        '-vcodec', 'mpeg4',
                        '-y', 'movie.mp4'
                        # To hide the logs
                              '-hide_banner',
                        '-loglevel', 'panic'
                        ])
