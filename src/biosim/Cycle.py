# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo
from biosim.Mapping import Jungle, Savannah


# from biosim.Herbivore_simulation import HSimulation


class Cycle:
    def __init__(self, input_map_matrix_with_pop):
        self.input_map_matrix_with_pop = input_map_matrix_with_pop

    def food_grows(self):
        map = Geo(input_map)
        # print(map.geo_ob_array)

        for row_of_obj in map.geo_ob_array:
            for obj in row_of_obj:

                if type(obj).__name__ == "Savannah":
                    # print(obj)
                    # print(obj.f_ij, obj.f_max)
                    obj.f_ij += obj.alpha * (obj.f_max - obj.f_ij)
                    # print(obj.f_ij, obj.f_max)
                elif type(obj).__name__ == "Jungle":
                    # print(obj)
                    # print(obj.f_ij, obj.f_max)
                    obj.f_ij = obj.f_max
                    # print(obj.f_ij, obj.f_max)

    # for hver celle:
    def animals_eat(self):
        """Herbevoirs and Carnevoirs eat"""
        # map = Geo(input_map)

        for row_of_obj in self.input_map_matrix_with_pop:
            for cell in row_of_obj:
                # print(cell)
                if type(cell).__name__ in ["Desert", "Savannah", "Jungle"]:
                    # print("Found")
                    # print(cell.animal_object_list)
                    herb_list= [animal for animal in cell.animal_object_list if \
                     type(animal).__name__ == "Herbivore"]
                    # print(herb_list)

                    herb_sorted = sorted(herb_list, key=lambda animal: animal.fitness,
                                     reverse=True)
                    # print(herb_sorted)

                    for herb in herb_sorted:
                        # print(herb.weight)
                        if herb.p['F'] <= cell.f_ij:
                            herb.weight += herb.p['beta'] * herb.p['F']
                            cell.f_ij -= herb.p['F']

# Eating for Carnivores after herbivores eat
#                     carn_list = [animal for animal in cell.animal_object_list if \
#                                  type(animal).__name__ == "Carnivore"]
#                     # print(carn_list)
#
#                     carn_sorted = sorted(carn_list, key=lambda animal: animal.fitness,
#                                          reverse=True)
#                     # print(carn_sorted)
#
#                     for carn in carn_sorted:
#                         herb_sorted_rev = sorted(herb_list, key=lambda animal: animal.fitness, reverse=True)
#                         for herb in herb_sorted_rev:
#                             if carn.F >= herb.weight:
#
#                                 if carn.fitness <= herb.fitness:
#                                     carn_kills = 0
#
#                                 elif 0 < carn.fitness - herb.fitness < carn.DeltaPhiMax:
#                                     carn_kills = (carn.fitness - herb.fitness)/carn.DeltaPhiMax
#
#                                 else:
#                                     carn_kills = 1
#
#                                 num = random.random()
#
#                                 if carn_kills >= num:
#                                     self.weigth += self.beta * herb.weigth
#                                     carn.fitness()
#                                     herb.is_dead = True
#                                     #remove from list




if __name__ == "__main__":
    si = Cycle()
    input_map = ("""\
                    OOOO
                    OJSO
                    OOOO""")
    ini_herbs = [{'loc': (1, 1),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(2)]}, {'loc': (1, 2),
                                                'pop': [
                                                    {'species': 'Herbivore',
                                                     'age': 5,
                                                     'weight': 20}
                                                    for _ in range(2)]}]
