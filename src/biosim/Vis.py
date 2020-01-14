# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Herbivore_simulation import HSimulation
from biosim.Geography import Geo

import matplotlib.pyplot as plt


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

        np.random.seed(seed)
        self._system = DiffSys(sys_size, noise)

        if img_dir is not None:
            self._img_base = os.path.join(img_dir, img_name)
        else:
            self._img_base = None
        self._img_fmt = img_fmt

        self._step = 0
        self._final_step = None
        self._img_ctr = 0

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

            #make subplots:
            #subplot(2,2,1)
            #subplot(2,2,2)
            #subplot(2,2,3)
            #subplot(2,2,4)
