import math
import os
import sys

# The required fuel is the mass of the module
# divided by three, rounded down and substracted by 2.
def formula(module_mass):
    return math.floor(int(module_mass)/3 - 2)


def fuelMass(mass):
    # If it's less than it's negligible.
    if mass <= 0:
        return 0
    else:
        return mass + fuelMass(formula(mass))


if __name__ == '__main__': 
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        part_1 = 0
        part_2 = 0

        for module in f.readlines():
            part_1 += formula(module)
            part_2 += fuelMass(formula(module))

        print("PART 1:", part_1)
        print("PART 2:", part_2)
