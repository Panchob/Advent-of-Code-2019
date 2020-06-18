import os
import sys
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from intcode.intCode_compiler import Intcode

GRID_SIZE = 50

if __name__ == '__main__':
    x = 0
    y = 0
    total = 0
    while x < GRID_SIZE:
        for y in range(GRID_SIZE):
            intcode = Intcode("input.txt")
            intcode.run(x)
            total += intcode.run(y)
        x += 1
    print(total)
        
            
            