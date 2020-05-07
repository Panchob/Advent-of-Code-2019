import math
import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    total_fuel = 0
    # The required fuel is the mass of the module
    # divided by three, rounded down and substracted by 2.
    for module in f.readlines():
        total_fuel += math.floor(int(module)/3) - 2

    print(total_fuel)
