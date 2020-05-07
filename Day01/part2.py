import math
import os
import sys


# From Day1.py
def formula(module_mass):
    return math.floor(int(module_mass)/3 - 2)


def fuelMass(mass):
    if mass <= 0:
        return 0
    else:
        return mass + fuelMass(formula(mass))

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    total_fuel = 0
    for module in f.readlines():
        total_fuel += fuelMass(formula(module))
    print (total_fuel)
