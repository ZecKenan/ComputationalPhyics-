

import pylab
import os
import math
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import random
from random import seed
from random import randint



# Number of runs
n = 10000

# Number of steps
N = 1000

# Recorded positions
rList = []

for ii in range(n):
  # Starting position
  posx = 0
  posy = 0
  posz = 0
  posw = 0

  # Record individual positions
  x = []
  y = []
  z = []
  w = []


  # Take N steps in stochastic directions
  for jj in range(N):
    value = random.randint(0,7)
    if value == 0:
      posx += 1

    elif value == 1:
      posx -= 1

    elif value == 2:
      posy += 1

    elif value == 3:
      posy -= 1

    elif value == 4:
      posz += 1

    elif value == 5:
      posz -= 1

    elif value == 6:
      posw += 1

    elif value == 7:
      posw -= 1

  # Append new positions to appropriate lists
    x.append(posx)
    y.append(posy)
    z.append(posz)
    w.append(posw)

  # Squared euclidian distances
  Rval = np.sum(np.array([posx, posy, posz, posw]) ** 2)

  # Add Rval to posList as integer
  rList.append(Rval)

mean_v = np.mean(rList)

p = np.log(mean_v)/np.log(N)

print(p)

fig = plt.figure()
#plt.plot(x,y,z)
ax = fig.gca(projection='3d')
ax.plot(x,y,z)
plt.title('3D Free Random Walk')
plt.show()
