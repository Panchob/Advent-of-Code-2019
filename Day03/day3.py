import os
import sys


def minDistance(wire1, wire2):
    intersections = set(wire1).intersection(wire2)
    distances = []
    for n in intersections:
        res = abs(n[0]) + abs(n[1])
        if res > 0:
            distances.append(res)
    return min(distances)


# Basically copied and pasted minDistance.
def minSteps(wire1, wire2):
    intersections = set(wire1).intersection(wire2)
    steps = []
    for n in intersections:
        res = abs(n[0]) + abs(n[1])
        if res > 0:
            # Since everything start at (0,0), the index is
            # the number of steps.
            steps.append(wire1.index(n) + wire2.index(n))
    return min(steps)


def positions(wire):
    board = [(0, 0)]
    for instruction in wire:
        # Instruction example: R75,D30,R83,U83,L12,D49,R71,U7,L72

        # Instead of calculating the line, just enumerate all
        # positions.
        direction = instruction[0]
        # Take the end of the string since the occurence can be
        # more than one char.
        occurence = int(instruction[1:])
        lastX = board[-1][0]
        lastY = board[-1][1]

        if direction == "U":
            for n in range(occurence):
                lastY += 1
                board.append((lastX, lastY))
        elif direction == "D":
            for n in range(occurence):
                lastY -= 1
                board.append((lastX, lastY))
        elif direction == "L":
            for n in range(occurence):
                lastX -= 1
                board.append((lastX, lastY))
        elif direction == "R":
            for n in range(occurence):
                lastX += 1
                board.append((lastX, lastY))
    return board

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    # First, store both wire in lists.
    wires = []
    for line in f:
        wires.append(line.split(","))

    # Map all positions for both wires
    wire1 = positions(wires[0])
    wire2 = positions(wires[1])

    # PART 1
    # Find all all the intersections and print the smallest one.
    print(minDistance(wire1, wire2))

    # PART 2
    # Use the same logic as in part one but return the smallest
    # number of steps.
    print(minSteps(wire1, wire2))
