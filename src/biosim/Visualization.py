# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Herbivore_simulation import HSimulation
from biosim.Geography import Geo
from simulation import BioSim

import matplotlib.pyplot as plt

map = ("""\
    OOOOO
    OJSDO
    OJSMO
    OJSDO
    OOOOO""")
ini_herbs = [{'loc': (1, 1), 'pop': [{'species': 'Herbivore', 'age': 5,
                                      'weight': 100} for _ in range(6)] + [
                                        {'species': 'Carnivore', 'age': 10,
                                         'weight': 500} for _ in range(2)
                                    ]}]
g = Geo(map)  # no particular use here
s = BioSim(map, ini_herbs, seed =1)
# print(s.object_matrix)
# print(g.geo_shape)

row_num = g.geo_shape[0]
column_num = g.geo_shape[1]
total_cells = row_num * column_num

print(row_num, column_num, total_cells)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
plt.subplots_adjust(wspace=0, hspace=0)

# color_dict ={"Ocean":"#1C53C4", "Desert":"#E3F315", "Savannah": "#C2FCD0",
#              "Jungle":"#79EE96", "Mountain":"#4A5757"}


# for f, att in enumerate(axs):
    # for j in att:
    #     j.set_xlim(0,1)
    #     j.set_ylim(0,20)
    #     j.set_xticks([])
    #     j.set_yticks([])

# for row, list_of_obj in enumerate(s.object_matrix):
#     for col, cell in enumerate(list_of_obj):
#         axs[row, col].set_facecolor(color_dict[type(cell).__name__])
#
# fig.savefig("plot.png")
# fig.show()

# herb_num = len([a for a in cell.animal_object_list
#                 if type(a).__name__ == "Herbivore"])
# carn_num = len([a for a in cell.animal_object_list
#                 if type(a).__name__ == "Carnivore"])
# print(row, col, type(cell).__name__, "H and C:", herb_num, carn_num)
# axs[row, col].bar([0.5, 1.5], [herb_num, carn_num], width=0.2)

# # axs[row,col].scatter(np.random.random(), np.random.random(), alpha=0.5)
# Update the plot, instead of replotting every time
