# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

class Eat:
    def __init__(self):
        pass

    def herb_eat(self, cell, herb):
        """Herbevoirs eat"""

        if herb.p['F'] <= cell.f_ij:
            herb.weight += herb.p['beta'] * herb.p['F']
            cell.f_ij -= herb.p['F']

        # elif 0 < cell.f_ij < self.F:
        #     self.weigth += self.beta * cell.f_ij
        #     cell.f_ij = 0
        #
        # elif cell.f_ij == 0:
        #     self.weigth = self.weigth

    # def carn_eat(self, cell):
    #     """Carnevoirs eat"""
    #
    #     herb_sorted_rev = sorted(cell.herb_list, key=lambda animal: animal.fitness, reverse=True)
    #     for herb in herb_sorted_rev:
    #
    #         if self.F >= herb.weigth:
    #
    #             if self.fitness > herb.fitness:
    #                 carn_kills = 0
    #
    #             elif 0 < self.fitness - herb.fitness < DeltaPhiMax:
    #                 carn_kills = uttrykk
    #
    #             else:
    #                 carn_kills = 1
    #
    #             if kills:
    #                 self.weigth += self.beta * herb.weigth
    #                 carn.fitness()
    #                 herb.is_dead = True
