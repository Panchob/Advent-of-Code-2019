import os
import sys
from intCode_compiler import Intcode

    

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:

    l = f.read().split(",")
    l = list(map(int, l))
    # I just added 0 until I had no out of bound exception.
    padding =  [0] * 1000
    memory = l + padding
    # Part one
    intCode1 = Intcode(memory)
    print("PART 1:", intCode1.run(1))
    # Part two
    intCode2 = Intcode(memory)
    print("PART 2:", intCode2.run(2))
        



    
