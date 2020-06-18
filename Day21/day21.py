import os
import sys
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from intcode.intCode_compiler import Intcode

class Springdroid:

    def __init__(self, computer):
        self.computer = computer
 
    def run(self, instructions):
        computer = self.computer
        for instruction in instructions:
            for i in map(ord, instruction):
                computer.run(i)
        return computer.run(10)


if __name__ == '__main__':

    intcode = Intcode("input.txt")
    spring = Springdroid(intcode)

    with open(os.path.join(sys.path[0], "script.txt"), "r") as s:
        instructions = []
        for line in s.readlines():
            instructions.append(line)
    
    print(chr(spring.run(instructions)))


                