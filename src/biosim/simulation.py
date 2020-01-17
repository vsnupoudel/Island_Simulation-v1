# -*- coding: utf-8 -*-

__author__ = "Anders Huse"
__email__ = "huse.anders@gmail.com"

from Cycle import Cycle
from Geography import Geo
from Visualization import Visualization
from Mapping import Savannah, Jungle
from Animal import Herbivore, Carnivore

import numpy as np
import matplotlib.pyplot as plt

class BioSim:
    def __init__(
        self,
        island_map,
        ini_pop,
        seed,
        ymax_animals=None,
        cmax_animals=None,
        img_base=None,
        img_fmt="png",
    ):
        """
        :param island_map: Multi-line string specifying island geography
        :param ini_pop: List of dictionaries specifying initial population
        :param seed: Integer used as random number seed
        :param ymax_animals: Number specifying y-axis limit for graph showing animal numbers
        :param cmax_animals: Dict specifying color-code limits for animal densities
        :param img_base: String with beginning of file name for figures, including path
        :param img_fmt: String with file type for figures, e.g. 'png'

        If ymax_animals is None, the y-axis limit should be adjusted automatically.

        If cmax_animals is None, sensible, fixed default values should be used.
        cmax_animals is a dict mapping species names to numbers, e.g.,
           {'Herbivore': 50, 'Carnivore': 20}

        If img_base is None, no figures are written to file.
        Filenames are formed as

            '{}_{:05d}.{}'.format(img_base, img_no, img_fmt)

        where img_no are consecutive image numbers starting from 0.
        img_base should contain a path and beginning of a file name.
        """
        self.seed = 1
        self.ini_pop = ini_pop
        self.island_map = Geo(island_map)
        self.object_matrix = self.island_map.object_matrix
        self.year = 0

        # Set the population in respective cell in the matrix
        for one_location_list in self.ini_pop:
            x, y = one_location_list['loc'][0], one_location_list['loc'][1]
            self.object_matrix[x][y].set_population(one_location_list)

    def set_animal_parameters(self, species, params):
        """
        Set parameters for animal species.

        :param species: String, name of animal species
        :param params: Dict with valid parameter specification for species
        """
        if species == 'Herbivore':
            Herbivore.up_par(params)

        else:
            Carnivore.up_par(params)

    def set_landscape_parameters(self, landscape, params):
        """
        Set parameters for landscape type.

        :param landscape: String, code letter for landscape
        :param params: Dict with valid parameter specification for landscape
        """
        if landscape == 'S':
            Savannah.parameters.update(params)
        else:
            Jungle.parameters.update(params)

    def simulate(self, vis_years=1, img_years=None, y_lim = 500):
        """
        Run simulation while visualizing the result.

        :param num_years: number of years to simulate
        :param vis_years: years between visualization updates
        :param img_years: years between visualizations saved to files (default: vis_years)

        Image files will be numbered consecutively.
        """
        c = Cycle(self.object_matrix)
#        v = Visualization(self.object_matrix)
#        v._set_graphics(y_lim)
#        v.create_map(self.island_matrix)

        step = 0

#        v.update_graphics(self.herbivore_distribution,
#                          self.carnivore_distribution,
#                          s.num_animals)

#        plt.savefig('Images\\Image-{0:03d}.{type}'.format(step, type="png"))

        while step < 20:
            c.food_grows()
            c.animals_eat()

            c.animals_reproduce()
            c.animals_migrate()
            c.animals_die()
#            v.update_graphics(self.herbivore_distribution,
#                              self.carnivore_distribution,
#                              s.num_animals)
#            plt.savefig('Images\\Image-{0:03d}.png'.format(step+1))

            step += 1
            self.year += 1
            # v._final_step += 1

#        v.make_movie()


    def add_population(self, population):
        """
        Add a population to the island

        :param population: List of dictionaries specifying population
        """
        for one_location_list in population:
            x, y = one_location_list['loc'][0], one_location_list['loc'][1]
            self.object_matrix[x][y].set_population(one_location_list)


    @property
    def current_year(self):
        return self.year


    @property
    def num_animals(self):
        """Number of herbivores in island"""
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
    def herbivore_distribution(self):
        """Pandas DataFrame with herbivore count for each cell on
        island."""
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
        """Pandas DataFrame with carnivore count for each
        cell on
        island."""
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
        """Pandas DataFrame with animal count for each
                cell on
                island."""
        # to be done later
        pass

    @property
    def island_matrix(self):
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
        pass
        """Create MPEG4 movie from visualization images saved."""


if __name__ == "__main__":
    map = """\
                 OOOOOOOOOOOOOOOOOOOOO
                 OOOOOOOOSMMMMJJJJJJJO
                 OSSSSSJJJJMMJJJJJJJOO
                 OSSSSSSSSSMMJJJJJJOOO
                 OSSSSSJJJJJJJJJJJJOOO
                 OSSSSSJJJDDJJJSJJJOOO
                 OSSJJJJJDDDJJJSSSSOOO
                 OOSSSSJJJDDJJJSOOOOOO
                 OSSSJJJJJDDJJJJJJJOOO
                 OSSSSJJJJDDJJJJOOOOOO
                 OOSSSSJJJJJJJJOOOOOOO
                 OOOSSSSJJJJJJJOOOOOOO
                 OOOOOOOOOOOOOOOOOOOOO"""


    ini_herbs = [
        {
            "loc": (10, 10),
            "pop": [
                {"species": "Herbivore", "age": 5, "weight": 20}
                for _ in range(20)
            ],
        }
    ]+ [
        {
            "loc": (10, 10),
            "pop": [
                {"species": "Carnivore", "age": 5, "weight": 70}
                for _ in range(50)
            ],
        }
    ]

    s = BioSim(map, ini_herbs, seed = 1)
    # print( len( s.object_matrix[10][10].animal_object_list) )

    s.add_population(ini_herbs)

    # print( len( s.object_matrix[10][10].animal_object_list) )

    # s.set_animal_parameters("Carnivore",
    #                         {
    #                             "a_half": 70,
    #                             "phi_age": 0.5,
    #                             "omega": 0.3,
    #                             "F": 65,
    #                             "DeltaPhiMax": 9.0,
    #                         }, )
    # s.set_animal_parameters("Herbivore", {"zeta": 3.2, "xi": 1.8})
    # print(Carnivore.p['F'])

    s.simulate()





