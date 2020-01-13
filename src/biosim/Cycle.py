# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

# from biosim.Geography import Geo
# from biosim.Mapping import Jungle, Savannah
import numpy as np

# from biosim.Herbivore_simulation import HSimulation
from biosim.Animal import Herbivore  # , Carnivore


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
                    herb_list = [animal for animal in cell.animal_object_list
                                 if type(animal).__name__ == "Herbivore"]

                    herb_sorted = sorted(herb_list,
                                         key=lambda animal: animal.fitness,
                                         reverse=True)
                    for herb in herb_sorted:
                        if cell.f_ij >= herb.p['F']:
                            herb.weight += herb.p['beta'] * herb.p['F']
                            cell.f_ij -= herb.p['F']
                        elif cell.f_ij < herb.p['F']:
                            herb.weight += herb.p['beta'] * cell.f_ij
                            cell.f_ij = 0

                    # carn logic here to be added later
                    carn_list = [animal for animal in cell.animal_object_list
                                 if type(animal).__name__ == "Carnivore"]

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

                    # calculate probabilty and new born
                    for animal in herb_list:
                        b_prob = min(1, animal.p['gamma'] *
                                     animal.fitness * (len(herb_list) - 1))
                        # print(b_prob)
                        # 1. check if random_number <= b_prob
                        # 2. check if the weight of parent is greater than...

                        if (np.random.random() <= b_prob) & \
                                (animal.weight >= animal.p['zeta'] * (
                                        animal.p['w_birth'] + animal.p[
                                    'sigma_birth'])):

                            baby_weight = np.random.normal(
                                animal.p['w_birth'], animal.p['sigma_birth'])

                            # 3. check if animal has sufficient weight
                            if animal.weight >= baby_weight * animal.p['xi']:
                                cell.animal_object_list.append(
                                    Herbivore(age=0, weight=baby_weight))
                                # reduce the parent weight by ...
                                animal.weight -= baby_weight * animal.p['xi']


if __name__ == "__main__":
    pass
