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

## First Assignment

# Number of runs
n = 10000

# Number of steps
N = 100

# Recorded positions
rList = []

# Number of runs
rNumber = []


Steps = []
times_at_finish = 0
for ii in range(n):

  visited = []
  steps_taken = 0
  prev = None
  moved = False

  # Starting position
  posx = 0
  posy = 0
  posz = 0
  visited.append([posx, posy, posz])
  x = []
  y = []
  z = []
  x.append(posx)
  y.append(posy)
  z.append(posz)


  # Take N steps in stochastic directions
  for jj in range(N):
    moved = False
    if jj > N-2:
      times_at_finish += 1

    while moved == False:
      value = random.randint(0,5)

      if value == 0 and prev != 1:
        if [posx+1, posy, posz] not in visited:
          prev = 0
          posx += 1
          steps_taken += 1
          visited.append([posx,posy, posz])
          x.append(posx)
          y.append(posy)
          z.append(posz)

          moved = True
        else:
          break

      elif value == 1 and prev != 0:
        if [posx-1, posy, posz] not in visited:
          prev = 1
          posx -= 1
          steps_taken += 1
          visited.append([posx,posy, posz])
          x.append(posx)
          y.append(posy)
          z.append(posz)

          moved = True
        else:
          break

      elif value == 2 and prev != 3:
        if [posx, posy+1, posz] not in visited:
          prev = 2
          posy += 1
          steps_taken += 1
          visited.append([posx,posy, posz])
          x.append(posx)
          y.append(posy)
          z.append(posz)

          moved = True
        else:
          break

      elif value == 3 and prev != 2:
        if [posx, posy-1, posz] not in visited:
          prev = 3
          posy -= 1
          steps_taken += 1
          visited.append([posx,posy, posz])
          x.append(posx)
          y.append(posy)
          z.append(posz)

          moved = True
        else:
          break

      elif value == 4 and prev != 5:
        if [posx, posy, posz+1] not in visited:
          prev = 4
          posz += 1
          steps_taken += 1
          visited.append([posx,posy, posz])
          x.append(posx)
          y.append(posy)
          z.append(posz)

          moved = True
        else:
          break

      elif value == 5 and prev != 4:
        if [posx, posy, posz-1] not in visited:
          prev = 5
          posz -= 1
          steps_taken += 1
          visited.append([posx,posy, posz])
          x.append(posx)
          y.append(posy)
          z.append(posz)

          moved = True
        else:
          break


  Steps.append(steps_taken)


  # Squared euclidian distances
  Rval = np.sum(np.array([posx, posy, posz]) ** 2) # add posz and posw

  # Add Rval to rList as integer
  rList.append(Rval)

  # Add number of steps in this run to appropriate list
  rNumber.append(steps_taken)

print("finished or W: " + str(times_at_finish))


# Compute values
mean_n = np.mean(rNumber) # this is mean steps taken
mean_v = np.mean(rList) # this is mean Rval
p = np.log(mean_v)/np.log(mean_n) # this is p value

# Print values
print('Mean rVal computed: ' + str(mean_v))
print('p-value: ' + str(p))

# Visualize steps
fig=plt.figure()
ax = p3.Axes3D(fig)
ax.plot(x,y,z)
plt.title('3D random walk')
# Compute entropy

c = Counter(Steps)
w = c[N]/float(N)
d = 3 # change to dimension
omg = w*((2*d)-1)**(N-2)
s = np.log(omg)/float(N-2)
print('s = ' + str(s))
