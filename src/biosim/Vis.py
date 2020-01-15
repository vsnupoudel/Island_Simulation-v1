# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Herbivore_simulation import HSimulation
from biosim.Geography import Geo

import matplotlib.pyplot as plt

DEFAULT_GRAPHICS_NAME = 'Plot'

class Vis:
    def __init__(self, sys_size, noise, seed,
                 img_dir=None, img_name=_DEFAULT_GRAPHICS_NAME,
                 img_fmt='png'):
        """
        :param sys_size:  system size, e.g. (5, 10)
        :type sys_size: (int, int)
        :param noise: noise level
        :type noise: float
        :param seed: random generator seed
        :type seed: int
        :param img_dir: directory for image files; no images if None
        :type img_dir: str
        :param img_name: beginning of name for image files
        :type img_name: str
        :param img_fmt: image file format suffix, default 'png'
        :type img_fmt: str
        """

#        np.random.seed(seed)
#        self._system = DiffSys(sys_size, noise)
#
#        if img_dir is not None:
#            self._img_base = os.path.join(img_dir, img_name)
#        else:
#            self._img_base = None
#        self._img_fmt = img_fmt
#
#        self._step = 0
#        self._final_step = None
#        self._img_ctr = 0
        self._DEFAULT_GRAPHICS_NAME = 'Plot'

        # the following will be initialized by _setup_graphics
        self._fig = None
        self._map_ax = None
        self._img_axis = None
        self._mean_ax = None
        self._mean_line = None

        def setup(self):
            """Creates subplots for plotting"""

            # create new figure window
            if self._fig is None:
                self._fig = plt.figure()

            if self._map_ax is None:
                self._map_ax = self._fig.add_subplot(2, 2, 1)
                self._img_axis = None

            if self._herb_ax is None:
                self._herb_ax = self._fig.add_subplot(2, 2, 2)
                self._img_axis = None
                # herb info

            if self._herb_ax is None:
                self._herb_ax = self._fig.add_subplot(2, 2, 3)
                self._img_axis = None
                # carn info

            if self._mean_ax is None:
                self._mean_ax = self._fig.add_subplot(2, 2, 4)
                self._mean_ax.set_ylim(0, 0.02)

            # needs updating on subsequent calls to simulate()
            self._mean_ax.set_xlim(0, self._final_step + 1)

            if self._mean_line is None:
                mean_plot = self._mean_ax.plot(np.arange(0, self._final_step),
                                               np.full(self._final_step,
                                                       np.nan))
                self._mean_line = mean_plot[0]
            else:
                xdata, ydata = self._mean_line.get_data()
                xnew = np.arange(xdata[-1] + 1, self._final_step)
                if len(xnew) > 0:
                    ynew = np.full(xnew.shape, np.nan)
                    self._mean_line.set_data(np.hstack((xdata, xnew)),
                                             np.hstack((ydata, ynew)))
