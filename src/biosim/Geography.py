# -*- coding: utf-8 -*-

"""
"""

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

import numpy as np 
import matplotlib.pyplot as plt

class GeographyArea:
	"""
	- Stores the size/shape of the geography, and the ID of each cell
	- ID of cell can be S,J,D,O,F (Savanna, Jungle, Desert, Ocean, Fjell)
	"""
	def __init__(self, geo_matrix_input_string ):
		self.geo_graph = geo_matrix_input_string

	@property
	def geo_shape(self):
		return shape( self.geo_graph)

	
	