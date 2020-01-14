# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo
# from biosim.Mapping import Jungle, Savannah
import numpy as np

# from biosim.Herbivore_simulation import HSimulation
from biosim.Animal import Herbivore, Carnivore


class Cycle:
    def __init__(self, object_matrix):
        """
        :param object_matrix: map with population, which is modified by each
        of the functions in this class in one after another
        """
        self.object_matrix = object_matrix

    def food_grows(self):
        """
        Updates/Increases:
        The amount of food available in Jungle and Savannah
        """
        for row_of_obj in self.object_matrix:
            for obj in row_of_obj:
                if type(obj).__name__ == "Savannah":
                    obj.f_ij += obj.alpha * (obj.f_max - obj.f_ij)
                elif type(obj).__name__ == "Jungle":
                    obj.f_ij = obj.f_max

    def animals_eat(self):
        """
        Herbivores and Carnivores eat once in every cycle
        This function updates:
        1. Increases the weight of animal if they eat
        2. Decreases the food in Savannah and Jungle if animals eat in that
        particular cell
        """

        for row_of_obj in self.object_matrix:
            for cell in row_of_obj:
                if type(cell).__name__ in ["Savannah", "Jungle"]:
                    herb_list = [animal for animal in cell.animal_object_list                #def her_eat
                                 if type(animal).__name__ == "Herbivore"]

                    herb_sorted = sorted(herb_list,
                                         key=lambda animal: animal.fitness,
                                         reverse=True)
                    for herb in herb_sorted:
                        herb.herb_eat(cell)


                    # Start for carnivores
                    """ This part should:
                    1. delete herbivores from cell after they are eaten
                    Conditions for carnivores eating
                    1. They eat until they get an amount F
                    2. If fitness is less than Herb, they can't kill that one
                    3. Kill with certain probability, if they have less than 
                    DeltaPhiMax fitness
                    4. They certainly kill otherwise
                    """
                    carn_list = [animal for animal in cell.animal_object_list                  #def carn_eat
                                 if type(animal).__name__ == "Carnivore"]
#                    print(carn_list)

                    carn_sorted = sorted(carn_list,
                                         key=lambda animal: animal.fitness,
                                         reverse=True)
#                    print(carn_sorted)

                    for carn in carn_sorted:
                        carn.carn_eat(cell)


    def animals_reproduce(self):
        """
        Loops through the whole map and makes animals reproduce if they
        meet the condition in each cell.
        This function updates:
        1. The number of animals in the particular cell
        2. The weight of the parents
        This function creates:
        1. New animal objects in the cell
        -----------------------------------------------------
        Rules for procreation:
        1. Probability min (1, gamma × F × (N − 1))
        """

        for row_of_obj in self.object_matrix:
            for cell in row_of_obj:
                if type(cell).__name__ in ["Desert", "Savannah", "Jungle"]:
                    # new_borns = 0
                    # Add new_borns for herbivores first
                    herb_list = [animal for animal in cell.animal_object_list
                                 if type(animal).__name__ == "Herbivore"]

                    new_herbs = []

                    # calculate probabilty and new born
                    for animal in herb_list:
                        new_herbs.append( animal.herb_reproduce(len(herb_list)))
                        # if animal.has_procreated == False:

                    for herb in new_herbs:
                        cell.animal_object_list.append(herb)

                    #def carn_reproduce

                    carn_list = [animal for animal in cell.animal_object_list
                                 if type(animal).__name__ == "Carnivore"]

                    new_carns = []

                    # calculate probabilty and new born
                    for animal in carn_list:
                        new_carns.append(animal.carn_reproduce(len(carn_list)))
                        # if animal.has_procreated == False:

                    for carn in new_carns:
                        cell.animal_object_list.append(carn)

    def get_adjacent_migratable_cells(self, row, column ):
        list_of_adj = []
        for i in (-1, 1):
            try:
                _t = self.object_matrix[row][column+i]
            except:
                pass
            else:
                if type(_t).__name__ in ["Desert", "Savannah", "Jungle"]:
                    list_of_adj.append(_t)

            try:
                _t = self.object_matrix[row+i][column]
            except:
                pass
            else:
                if type(_t).__name__ in ["Desert", "Savannah", "Jungle"]:
                    list_of_adj.append(_t)

        return list_of_adj

    def animals_migrate(self):
        """
        :param : self, the map object with all the cells and all the animals
        This function accomplishes the following
        - Delete migrated animals from current cell
        - Add incoming animals to the new cell

        :return: None

        """

        for row, row_of_obj in enumerate(self.object_matrix):
            for col, cell in enumerate(row_of_obj):
                animals_moved_away = []
                if type(cell).__name__  in ["Desert","Savannah", "Jungle"]:
                    adj_cells = self.get_adjacent_migratable_cells(row, col)
                    # Propensity calculation for each adjacent cell
                    propen_list_h = []
                    for cel in adj_cells:
                        propen_list_h.append(cel.pi_ij_herb)

                    propen_list_c = []
                    for cel in adj_cells:
                        propen_list_c.append(cel.pi_ij_carn)

                    # propability calculation for each adjacent cell
                    proba_list_h = np.array(propen_list_h) / np.sum(propen_list_h)
                    proba_list_c = np.array(propen_list_c) / np.sum(propen_list_c)

                    # Animal migrates only if it passes probability

                    for animal in cell.animal_object_list:
                        print(animal, animal.p['mu'] , animal.fitness)
                        move_prob = animal.p['mu'] * animal.fitness
                        rand_num = np.random.random()

                        if (rand_num <= move_prob) & (animal.has_migrated == False):
                            if type(animal).__name__ == "Herbivore":
                                animal.herb_migrates(cell, adj_cells, proba_list_h)
                                # cum_prop = 0
                                # val = np.random.random()
                                # for i, prob in enumerate(proba_list_h):
                                #     cum_prop += prob
                                #     if val <= cum_prop:
                                #         new_cell = adj_cells[i]
                                #         new_cell.animal_object_list.append(animal)
                                #         break

                            if type(animal).__name__ == "Carnivore":
                                animal.carn_migrates(cell, adj_cells, proba_list_c)
                                # cum_prop = 0
                                # val = np.random.random()
                                # for i, prob in enumerate(proba_list_c):
                                #     cum_prop += prob
                                #     if val <= cum_prop:
                                #         new_cell = adj_cells[i]
                                #         new_cell.animal_object_list.append(animal)
                                #         break

                            animal.has_moved = True
                            animals_moved_away.append(animal)

                cell.animal_object_list = [animal for animal in cell.animal_object_list if
                                           animal not in animals_moved_away]



if __name__ == "__main__":
    map = ("""\
        OOOOO
        OJSDO
        OJSJO
        OJSDO
        OOOOO""")
    c = Cycle(map)

    c.animals_migrate()
