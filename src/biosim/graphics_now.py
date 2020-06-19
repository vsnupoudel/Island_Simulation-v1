# -*- coding: utf-8 -*-
"""Class with plotting methods"""

__author__ = "Bishnu Poudel"
__email__ = "bipo@nmbu.no"

import numpy as np
import matplotlib.pyplot as plt

# Inputs to class are island, number of animals, current year, distribution of age, weight, fitness
# Output is a graph with 7 plots and a text that shows the current year


class InitGraphics():
    def __init__(self):
        self._fig = plt.figure(figsize=(8, 6.4))
        self._gs = self._fig.add_gridspec(nrows=5, ncols=6, left=0.08, right=0.96,
                                          bottom=0.05, top=0.95, wspace=0.6, hspace=0.8)
        self._year_info = _TimeInfo(self._fig, self._gs[0, 2:4])

        plt.draw()


class _TimeInfo:
    info_fmt = 'Year: {:5d}'

    def __init__(self, fig, gspec):
        self._ax = fig.add_subplot(gspec)
        self._ax.axis('off')
        self._text = self._ax.text(0.5, 0.5, self.info_fmt.format(0),
                                   verticalalignment='center', horizontalalignment='center',
                                   transform=self._ax.transAxes)

    def update(self, year):
        self._text.set_text(self.info_fmt.format(year))
