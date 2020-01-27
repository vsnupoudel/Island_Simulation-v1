# -*- coding: utf-8 -*-
"""User facing class! Has simulate function and several useful properties"""

__author__ = "Anders Huse"
__email__ = "huse.anders@gmail.com"

from .cycle import Cycle
from .geography import CreateMap
from .visualization import Visualization
from .terrain import Savannah, Jungle
from .animal import Herbivore, Carnivore

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
                           color-code limits for animal densities
    :ivar total_years:     int(default, 60), total number of years for all the
                           sub-simulations
    :ivar img_base:         Path relative to the code being run, where the user
                            intends to store the images. Also can specify the
                            whole path of the computer. If is none,
                            no image is stored.
    :ivar img_fmt:         str(default, png), image fmt

    :ivar num_images:      int(default, 0), number of images
    :ivar object_matrix:   list, 2D list of cell objects containing
                           herbivores and carnivores

    :ivar viz:              Instance of Visualization class
    :ivar viz.set_graphics:   Graphics are set

    """

    def __init__(
            self,
            island_map,
            ini_pop,
            seed=1,
            ymax_animals=12000,
            total_years=500,
            img_base=None,
            img_fmt="png",
            cmax_animals=None
    ):
        """
        :param island_map: Multi-line string specifying island geography
        :param ini_pop: List of dictionaries specifying initial population
        :param seed: Integer used as random number seed
        :param ymax_animals: Number specifying y-axis limit for graph
                             showing total animal numbers, default is
                             ten thousand
        :param total_years: The xlimit of the line graph, should specify total
                            number of year for which the user wants to
                            simulate, default = 60
        :param img_base: Path relative to the code being run, where the user
                         intends to store the images. Also can specify the
                         whole path of the computer. If is none,
                         no image is stored.
        :param img_fmt: String with file type for figures, e.g. 'png'
        :param cmax_animals: Dict specifying color-code limits for animal
                             densities

        total_years should be greater than the sum of individual years of
        simulations.

        """
        self.num_images = 0
        self.current_year = 0
        self.seed = seed
        self.ini_pop = ini_pop
        self.island_map = CreateMap(island_map)
        self.object_matrix = self.island_map.object_matrix
        self.ymax_animals = ymax_animals
        self.total_years = total_years
        self.img_fmt = img_fmt
        self.img_base = img_base
        self.cmax_animals = cmax_animals
        if self.cmax_animals is None:
            self.cmax_animals = {'Herbivore': 50, 'Carnivore': 50}

        # Set the population in respective cell in the matrix
        for one_location_list in self.ini_pop:
            x, y = one_location_list['loc'][0], one_location_list['loc'][1]
            self.object_matrix[x][y].set_population(one_location_list)

        self.viz = Visualization()
        self.viz.set_graphics(self.ymax_animals, self.total_years)

        if self.img_base:
            if os.path.exists(self.img_base):
                for root, dirs, files in os.walk(self.img_base, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))

    @staticmethod
    def set_animal_parameters(species, params):
        """
        Set parameters for animal species.
        :param species:  string, name of animal species
        :param params:   dict, valid parameter specification for species
        """
        if species == "Herbivore":
            Herbivore.up_par(params)
        elif species == "Carnivore":
            Carnivore.up_par(params)

    @staticmethod
    def set_landscape_parameters(landscape, params):
        """
        Set parameters for landscape type.

        :param landscape:   string, code letter for landscape
        :param params:      dict, parameter specification for landscape
        """
        if landscape == "S":
            Savannah.update_par(params)
        elif landscape == "J":
            Jungle.update_par(params)

    def simulate(self, num_years=20, vis_years=1, img_years=1):
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
        """

        self.viz.create_map(self.island_matrix)

        step = 0
        self.viz.update_graphics(self.herbivore_distribution,
                               self.carnivore_distribution,
                               self.num_animals_per_species,
                               self.cmax_animals)
        if self.img_base:
            if not os.path.exists(self.img_base):
                os.makedirs(self.img_base)
            plt.savefig('{}\\_{:05d}.{}'.format(self.img_base, self.num_images,
                                                self.img_fmt))
        self.num_images += 1
        c = Cycle(self.object_matrix)
        while step <= num_years:
            # print([a.fitness for a in c.object_matrix[10][
            #     10].animal_object_list])
            c.food_grows()
            c.animals_eat()
            c.animals_reproduce()
            c.animals_migrate()
            c.animals_die()
            c.animals_age()
            self.viz.update_graphics(self.herbivore_distribution,
                                   self.carnivore_distribution,
                                   self.num_animals_per_species,
                                   self.cmax_animals)

            step += 1
            self.current_year += 1

            if (step % img_years == 0) & (self.img_base is not None):
                plt.savefig('{}\\_{:05d}.{}'.format(self.img_base,
                                                    self.num_images,
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
        current year on the simuation island

        :return:  current year, int
        """
        return self.current_year

    @property
    def num_animals_per_species(self):
        """
        Total number of herbivores and carnivores on island

        :return: animals_count_dict  dict, dictionary containing number of
                                     herbivores and carnivores on island
        """
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
        """
        :return: the sum of total animals in the entire island
        """
        return (self.num_animals_per_species['Herbivore'] +
                self.num_animals_per_species['Carnivore'])

    @property
    def herbivore_distribution(self):
        """2D matrix with herbivore count for each cell on the island."""
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
        """2D matrix with carnivore count for each cell on the island."""
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
        herb_flat = self.herbivore_distribution.flatten().astype(int)
        carn_flat = self.carnivore_distribution.flatten().astype(int)

        rows = np.shape(self.object_matrix)[0]
        columns = np.shape(self.object_matrix)[1]
        row_nums = [r for r in range(rows) for _ in range(columns)]
        col_nums = [c for _ in range(rows) for c in range(columns)]

        _df = pd.DataFrame(list(zip(row_nums, col_nums, herb_flat, carn_flat)),
                           columns=['Row', 'Col', 'Herbivore', 'Carnivore'],
                           index=None)
        return _df

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

    def make_movie(self, full_path_and_file=None):
        """
        Makes a movie of a series of images

        :param full_path_and_file: full path, including filename of
                                    the ffmpeg.exe file
         """
        if full_path_and_file is None:
            full_path_and_file = r'ffmpeg'

        subprocess.run([full_path_and_file,
                        '-f', 'image2',
                        '-r', '3',
                        '-i', self.img_base+'\\_%05d.png',
                        '-vcodec', 'mpeg4',
                        '-y', 'Simulation_movie_2.mp4',
                        # To hide the logs
                              '-hide_banner',
                        '-loglevel', 'panic'
                        ])
