# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"


import numpy as np



class Cycle:
    def __init__(self, object_matrix):
        """
        :param object_matrix: map with population, which is modified by each
        of the functions in this class in the order of definition
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
                    # print('food grow in Savannah')
                    obj.f_ij += obj.alpha * (obj.parameters['f_max'] -
                                             obj.f_ij)
                elif type(obj).__name__ == "Jungle":
                    obj.f_ij = obj.parameters['f_max']
                    # print('food grow in Jungle')

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

                    herb_sorted = sorted(cell.herb_list,
                                         key=lambda animal: animal.fitness,
                                         reverse=True)

                    for herb in herb_sorted:
                        herb.herb_eat(cell)

                    # Carnivores of the cell start eating
                if type(cell).__name__ in ["Savannah", "Jungle", "Desert"]:

                    carn_sorted = sorted(cell.carn_list,
                                         key=lambda animal: animal.fitness,
                                         reverse=True)

                    for carn in carn_sorted:
                        # additional logic to be added later
                        # currently the Carnivore eats 1 herbivore only
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
                    new_herbs = []
                    # print('rep')

                    # calculate probabilty and new born
                    # print('object_list', cell.animal_object_list)
                    # print('herb_list', cell.herb_list)
                    for animal in cell.herb_list:
                        # print(animal)
                        new = animal.herb_reproduce(cell.n_herbs)
                        # print('new')
                        if new:
                            # print('Herb rep')
                            new_herbs.append(new)
                        # if animal.has_procreated == False:

                    for herb in new_herbs:
                        cell.animal_object_list.append(herb)

                    # For carn_reproduce

                    new_carns = []
                    # calculate probabilty and new born
                    for animal in cell.carn_list:
                        # print('Carn rep')
                        new = animal.carn_reproduce(cell.n_carns)
                        if new:
                            # print('Carn rep')
                            new_carns.append(new)
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
                    for _c in adj_cells:
                        propen_list_h.append(_c.pi_ij_herb)

                    propen_list_c = []
                    for _c in adj_cells:
                        propen_list_c.append(_c.pi_ij_carn)

                    # propability calculation for each adjacent cell
                    proba_list_h = np.array(propen_list_h) / np.sum(propen_list_h)
                    proba_list_c = np.array(propen_list_c) / np.sum(propen_list_c)

                    # Animal migrates only if it passes probability

                    for animal in cell.animal_object_list:
                        # print(cell.row, cell.column, animal, animal.p['mu'] ,
                        #       animal.fitness)
                        move_prob = animal.p['mu'] * animal.fitness #should
                        # be property
                        rand_num = np.random.random()

                        if (rand_num <= move_prob) & (animal.has_migrated == False):
                            if type(animal).__name__ == "Herbivore":
                                animal.herb_migrates(animal, cell, adj_cells,
                                                     proba_list_h)

                            if type(animal).__name__ == "Carnivore":
                                # print('Carn migrates called')
                                animal.carn_migrates(animal, cell, adj_cells,
                                                     proba_list_c)

                            animal.has_migrated = True
                            animals_moved_away.append(animal)

                cell.animal_object_list = [animal for animal in
                                           cell.animal_object_list if
                                           animal not in animals_moved_away]

    def animals_die(self):
        death_list = []
        for row, row_of_obj in enumerate(self.object_matrix):
            for col, cell in enumerate(row_of_obj):
                if type(cell).__name__ in ["Desert", "Savannah", "Jungle"]:
                    for animal in cell.animal_object_list:
                        if animal.fitness == 0:
                            death_list.append(animal)
                        else:
                            death_prob = animal.p['omega']*(1- animal.fitness)
                            rand_num = np.random.random()
                            if rand_num < death_prob:
                                death_list.append(animal)

                cell.animal_object_list = [animal for animal in
                                           cell.animal_object_list if
                                           animal not in death_list]




if __name__ == "__main__":
    map = ("""\
        OOOOO
        OJSDO
        OJSJO
        OJSDO
        OOOOO""")
    c = Cycle(map)

    c.animals_migrate()
