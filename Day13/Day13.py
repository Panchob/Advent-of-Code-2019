import os
import sys
from intCode_compiler import Intcode
import pygame

class Tile:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
    

def createGame(intCode):
    tiles = []
    blocks = 0
    tile = [0, 0, 0]

    while not intCode.stopped and not intCode.waiting:
        for i in range(3):
            tile[i] = intCode.run()
        if not intCode.waiting:
            tiles.append(Tile(tile[0], tile[1], tile[2]))
    return tiles

def numberOfBlocks(tiles):
    nBblocks = 0
    for tile in tiles:
        if tile.id == 2:
            nBblocks += 1
    return nBblocks

if __name__ == '__main__': 
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:

        lst = f.read().split(",")
        lst = list(map(int, lst))
        padding =  [0] * 100000
        l = lst + padding
        intCode = Intcode(l)
        pygame.init()

        #Run the intCode to set the stage
        game = createGame(intCode)

        font = pygame.font.Font(None, 36)
        # Set up the drawing window
        screen = pygame.display.set_mode([1320, 600])

        # Part 1
        print("Number of starting blocks:", numberOfBlocks(game))

        # Part 2
        # Run until the user asks to quit
        running = True
        ball = 0
        paddle = 0
        score = 0
        input = 0
        screen.fill((0, 0, 0))
        # TODO: Extract following code in a function
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for tile in game:
                if tile.x == -1 and tile.y == 0:
                    score = tile.id
                elif tile.id == 0:
                    color = (0, 0, 0)
                elif tile.id == 1:
                    color = (255, 255, 255)
                elif tile.id == 2:
                    color = (245, 66, 99)
                elif tile.id == 3:
                    paddle = tile.x
                    color = (255, 255, 255)
                elif tile.id == 4:
                     ball = tile.x
                     color = (255, 255, 255)

                pygame.draw.rect(screen, color, [tile.x*30, tile.y*30, 30, 30])
                text = font.render(str(score), 1, color)
                
                textpos = text.get_rect(centerx=screen.get_width()/2)
                # FIXME: The score stack onto the last one.
                screen.blit(text, textpos)

            if ball < paddle:
                 input = -1
            elif ball > paddle:
                input = 1
            else:
                input = 0
                
            intCode.setInput(input)
            game = createGame(intCode)

            if intCode.stopped:
                running = False

            # Flip the display
            pygame.display.flip()
            pygame.time.Clock().tick(150)
        # FIXME: score is one short
        print(score)

        
        



    
