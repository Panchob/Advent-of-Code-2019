import numpy as np
import math
import os
import sys
from collections import defaultdict
            
ASTEROIDX = 11
ASTEROIDY = 13

def asteroidCount(arr, curr):
   rad = 0
   angles = defaultdict(list)

   #print("Now calculating position: ", curr)

   for j in range(len(arr)):
      for i in range(len(arr[0])):
         if arr[i][j] == '#':
            deg = math.atan2(curr[0] - i, curr[1] - j) * 180 / math.pi
            angles[deg].append((i, j))
   return(angles)
             

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:

   matrix = []
   for line in f:
      for c in line.splitlines():
         matrix.append(c)
   arr = np.array(matrix)

   total = []
   maximum = (0,0)
   mcount = 0
   for j in range(len(arr)):
      for i in range(len(arr[0])):
         if arr[i][j] == '#':
            total = asteroidCount(arr, (i,j))
            if len(total) > mcount:
               mcount = len(total)
               anglespt2 = total
               maximum = (i, j)

   #PART ONE
   print(mcount)
   print(maximum)

   first = []
   second = []
   third = []
   fourth = []

   for key in sorted(anglespt2.keys()):
      if key >= 0 and key <= 90:
         first.append(key)
      elif key < 0 and key >= -90:
         second.append(key)
      elif key < -90 and key >= -180:
         third.append(key)
      elif key > 90 and key <= 180:
         fourth.append(key)

   keys = first + second + third + fourth
   #print(keys)

   i = 0
   while i < 200:
      for key in keys:
         current = anglespt2[key]
         maxDis = 10000000000
         toRemove = current[0]
         for point in current:
            dis = math.sqrt((point[0] - ASTEROIDX)**2 + (point[1] - ASTEROIDY)**2)
            if dis <= maxDis:
               maxDis = dis
               toRemove = point
         print(i, toRemove)
         current.remove(toRemove)
         i += 1
         if i == 200:
            break


