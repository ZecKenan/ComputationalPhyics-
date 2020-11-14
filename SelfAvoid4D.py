import pylab
import os
import math
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
import random
from random import seed
from random import randint
from decimal import Decimal
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.text import OffsetFrom



# Number of runs
n = 10000

# Number of steps
N = 100

# Recorded positions
rList = []

# Number of runs
rNumber = []


Steps = []
for ii in range(n):
  # Stored previous locations
  visited = []
  steps_taken = 0
  prev = None
  moved = False

  # Starting position
  posx = 0
  posy = 0
  posz = 0
  posw = 0
  visited.append([posx, posy, posz, posw])
  x = []
  y = []
  z = []
  w = []
  x.append(posx)
  y.append(posy)
  z.append(posz)
  w.append(posw)


  # Take N steps in stochastic directions
  for jj in range(N):

    moved = False

    while moved == False:
      value = random.randint(0,7)
      if value == 0 and prev != 1:
        prev = 0
        posx += 1
        steps_taken += 1
        moved = True

      elif value == 1 and prev != 0:
        prev = 1
        posx -= 1
        steps_taken += 1
        moved = True

      elif value == 2 and prev != 3:
        prev = 2
        posy += 1
        steps_taken += 1
        moved = True

      elif value == 3 and prev != 2:
        prev = 3
        posy -= 1
        steps_taken += 1
        moved = True

      elif value == 4 and prev != 5:
        prev = 4
        posz += 1
        steps_taken += 1
        moved = True

      elif value == 5 and prev != 4:
        prev = 5
        posz -= 1
        steps_taken += 1
        moved = True

      elif value == 6 and prev != 7:
        prev = 6
        posw += 1
        steps_taken += 1
        moved = True

      elif value == 7 and prev != 6:
        prev = 7
        posw -= 1
        steps_taken += 1
        moved = True



    if moved:
      if [posx, posy, posz, posw] in visited:
        break
      else:
        visited.append([posx,posy, posz, posw])
        x.append(posx)
        y.append(posy)
        z.append(posz)
        w.append(posw)

    Steps.append(steps_taken)

    #For debugging this step
    #if jj == 49:
    #  print(str(ii))


  # Squared euclidian distances
  Rval = np.sum(np.array([posx, posy, posz, posw]) ** 2) # add posz and posw

  # Add Rval to rList as integer
  rList.append(Rval)

  # Add number of steps in this run to appropriate list
  rNumber.append(steps_taken)

"""# Visualization & Calculations"""

# Compute values
mean_n = np.mean(rNumber) # this is mean steps taken
mean_v = np.mean(rList) # this is mean Rval
p = np.log(mean_v)/np.log(mean_n) # this is p value

# Print values
print('Mean steps taken: ' + str(mean_n))
print('Mean rVal computed: ' + str(mean_v))
print('p-value: ' + str(p))

# Compute entropy
c = Counter(Steps)
print("This is c(N) " + str(c[N]))
w = c[N]/float(n)
print("This is W " + str(w))
d = 4 # change to dimensions

omg = w*((2*d)-1)**(N-2)
s = np.log(omg)/float(N-2)
print('s = ' + str(s))


c = Counter(Steps) # count how many times different steps have been taken
