import os
import sys
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from intcode.intCode_compiler import Intcode

class Springdroid:

    def __init__(self, computer):
        self.computer = computer
    

    
    def run(self, instructions):
        out = []
        computer = self.computer

        while not computer.waiting:
            out.append(computer.run())

        print("".join([chr(o) for o in out[:-1]]))


        for instruction in instructions:
            for i in map(ord, instruction):
                out.append(chr(computer.run(i)))


if __name__ == '__main__':

    intcode = Intcode("input.txt")
    spring = Springdroid(intcode)

    with open(os.path.join(sys.path[0], "script.txt"), "r") as s:
        instructions = []
        for line in s.readlines():
            instructions.append(line)
    
    spring.run(instructions)


                