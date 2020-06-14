import os
import sys
from intCode_compiler import Intcode

GRID_SIZE = 50

if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        l = f.read().split(",")
        l = list(map(int, l))
        padding =  [0] * 10000
        memory = l + padding

    x = 0
    y = 0
    total = 0
    while x < GRID_SIZE:
        for y in range(GRID_SIZE):
            intcode = Intcode(memory)
            intcode.input = x
            intcode.run()
            intcode.input = y
            total += intcode.run()
        x += 1
    print(total)
        
            
            