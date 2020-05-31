import os
import sys
from intCode_compiler import Intcode

DIRECTIONS = [1,2,3,4]
path = []
validPaths = []
visited = []


class Node:
    def __init__(self, position, lastDirection):
        self.position = position
        self.lastDirection = lastDirection
    
#List all possible paths
def updateGraph(current, intCode):
    visited.append(current.position)
    for direction in DIRECTIONS:
        if direction == reverse(current.lastDirection):
            continue
        result = intCode.run(direction)
        x, y = current.position
        if result != 0:
            if direction == 1:
                y += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            elif direction == 4:
                x += 1

            if result == 2:
                print(x,y)
                validPaths.append(len(path))
                break
                
            path.append(direction)
            updateGraph(Node((x,y), direction), intCode)
            
    if path:
        path.pop()
        intCode.run(reverse(current.lastDirection))
    

        
def reverse(direction):
    r = 0
    if direction == 1:
        r = 2
    elif direction == 2:
        r = 1
    elif direction == 3:
        r = 4
    elif direction == 4:
        r = 3
    return r
    
if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        l = f.read().split(",")
        l = list(map(int, l))

        padding =  [0] * 1000
        memory = l + padding
        intCode = Intcode(memory)

        current = Node((0,0),0)
        updateGraph(current, intCode)

    print(validPaths)
