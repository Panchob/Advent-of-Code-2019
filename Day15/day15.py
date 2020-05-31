import os
import sys
import pygame
from intCode_compiler import Intcode


DIRECTIONS = [1, 4, 2, 3]
Y = [1, 0, -1, 0]
X = [0, 1, 0, -1]

path = []
validPaths = []
visited = []
TILE = 10
        
def turnRight(i):
    i += 1
    if i > 3:
        i = 0
    return i

def turnLeft(i):
    i -= 1
    if i < 0:
        i = 3
    return i
    
if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        l = f.read().split(",")
        l = list(map(int, l))

        padding =  [0] * 1000
        memory = l + padding

    robot = Intcode(memory)
    current = (25,25)
    start = (25,25)
    world = {current: "empty"}
    path = [start]
    isGoalReached = False
    goal = None
    direction = 0

    screen = pygame.display.set_mode([600, 600])
    tiles = {}
    tileTypes = ["empty", "wall", "robot", "start", "path", "goal"]
    tileColors = ["white", "black", "blue", "orange", "green", "red"]
    for i in range(6):
        tiles[tileTypes[i]] = pygame.Surface((TILE, TILE))
        tiles[tileTypes[i]].fill(pygame.Color(tileColors[i]))
    
    mapExplored = False
    running = True

    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        x, y = current
        x += X[direction]
        y += Y[direction]
        
        if (x, y) == start:
            running = False

        result = robot.run(DIRECTIONS[direction])
        if result > 0:
            if (x,y) in world:
                if not isGoalReached:
                    path.pop()
            else:
                world[(x,y)] = "empty"
                if result == 2:
                    print(len(path))
                    goal = (x, y)
                    isGoalReached = True
                if not isGoalReached:
                    path.append((x,y))

            direction = turnLeft(direction)
            current = (x, y)
        else:
            direction = turnRight(direction)
            world[(x,y)] = "wall"
            
            # TODO export in a function
            screen.fill(pygame.Color("grey50"))
            for  x, y in world:
                type = world[x, y]
                screen.blit(tiles[type], (x * TILE, y * TILE))
            for  x, y in path:
                screen.blit(tiles["path"], (x * TILE, y * TILE))
            x,y = current
            screen.blit(tiles["robot"], (x * TILE, y * TILE))
            x,y = start
            screen.blit(tiles["start"], (x * TILE, y * TILE))
            if goal:
                x, y = goal
                screen.blit(tiles["goal"], (x * TILE, y * TILE))


            pygame.display.flip()
            pygame.time.Clock().tick(120)
    

