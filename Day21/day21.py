from intCode_compiler import Intcode
import os
import sys

class Springdroid:

    def __init__(self, computer):
        self.computer = computer
 
    def run(self, instruction):
        self.computer.intput = "".join(map(str, map(ord, instruction)))
        return self.computer.run()


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        l = f.read().split(",")
        l = list(map(int, l))
        padding =  [0] * 10000
        memory = l + padding

intcode = Intcode(memory)
spring = Springdroid(intcode)

print(chr(spring.run("WALK")))