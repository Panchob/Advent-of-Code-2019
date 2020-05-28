import os
import sys
import queue
from intCode_compiler import Intcode

class Node:
    def __init__(self, position, path=[]):
        self.position = position
        self.visited = False
        self.path = path

DIRECTIONS = [1,2,3,4]
# Use a queue to visited all that is near current node first.
actions = queue.Queue()
    
if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:

        l = f.read().split(",")
        l = list(map(int, l))

        padding =  [0] * 1000
        memory = l + padding

        intcode = Intcode(memory)

        current = Node((0,0))
        current.visited = True

        # Create first nodes and paths
        for direction in DIRECTIONS:
            x,y = current.position
            if direction == 1:
                y += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            elif direction == 4:
                x += 1

            path = current.path
            path.append(direction)
            actions.put(Node((x,y), path))
