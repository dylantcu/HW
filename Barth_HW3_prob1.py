# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 00:06:14 2017

@author: dylanbarth
"""

import numpy as np
from matplotlib import pyplot as p

array = np.loadtxt("stm.txt")
p.imshow(array, cmap="cubehelix")
p.savefig("CubeHelix_HM")
p.show()