import os
import sys
from Intcode import Intcode

    

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:

    intCode = Intcode("input.txt")
    intCode.run(1)
    print("PART 1:", intCode.getOutput()[0])

    intCode = Intcode("input.txt")
    intCode.run(2)
    print("PART 2:", intCode.getOutput()[0])

        



    
