import math
import os
import sys

def formula(module_mass):
    return math.floor(int(module_mass)/3 - 2)


def fuelMass(mass):
    if mass <= 0:
        return 0
    else:
        return mass + fuelMass(formula(mass))


if __name__ == '__main__':
    part1 = 0
    part2 = 0

    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:

        for module in f.readlines():
            # Get the total mass of fuel used to send the rocket
            # in orbit.
            part1 += formula(module)
            
            # Same thing, but including the fuel mass as well.
            part2 += fuelMass(formula(module))

    print("PART 1:", part1)
    print("PART 2:", part2)
