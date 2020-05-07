import sys
import os
from intCode_compiler import Intcode
from tkinter import *


def paint(firstInput, part2):
    paints = {}
    # Yup, pretty straightforward, but hey, that works.
    direction = ["U", "R", "D", "L"]

    angle = 0
    # Starting position
    x = 50
    y = 50

    input = firstInput
    intCode = Intcode(l)
    while not intCode.stopped:
        # First output
        out = intCode.run(input)
        if out == 0:
            paints[(x, y)] = 0
        else:
            paints[(x, y)] = 1

        # Second output
        out = intCode.run(input)

        # I just use an array containing the directions,
        # instead of implementing real angles
        # (I did that enough in day 10...).
        if out == 0:
            if angle + 1 == len(direction):
                # Aka poor's man linked list
                angle = 0
            else:
                angle += 1
        else:
            if angle - 1 < 0:
                angle = 3
            else:
                angle -= 1

        # Here I increment by a little more of the width of the
        # squares so it's easily readable. It's change nothing for part 1
        # since its stored as is in the dictionary
        if direction[angle] == "U":
            y -= 25
        elif direction[angle] == "R":
            x -= 25
        elif direction[angle] == "D":
            y += 25
        elif direction[angle] == "L":
            x += 25

        if (x, y) in paints:
            input = paints[(x, y)]
        else:
            input = 0

    return paints


with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lst = f.read().split(",")
    lst = list(map(int, lst))
    padding = [0] * 1000
    l = lst + padding

    # Part 1
    paints = paint(0, False)
    print("PART 1: The robots moves", len(paints), "times")

    # Part 2
    paints = paint(1, True)
    canvas = Tk()
    canvas.title("Points")
    c = Canvas(canvas,
               width=1150,
               height=275)
    c.pack(expand=1, fill=BOTH)

    for k, v in paints.items():
        x, y = k
        if v == 1:
                c.create_rectangle(x, y, x + 20, y + 20,
                                   outline="#fb0", fill="#fb0")

    mainloop()
