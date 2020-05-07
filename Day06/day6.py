import os
import sys
from collections import defaultdict

# I use global variable to simplify my recursive functions.
global objects_p1
global objects_p2
global total
global visited


# Depth first search, not necessarily the shortest path, but work with my data.
def pathBetween(current, destination, path):
    visited[current] = True
    path.append(current)

    for orbit in objects_p2[current]:
        if orbit == destination:
            print("Minimal orbital transfer:", len(path))
            break
        elif visited[orbit] is False:
            pathBetween(orbit, destination, path)

    path.pop()
    visited[current] = False


# Algorithm to count number of child a node has in a tree.
# It wil loop on all nodes a store each count in "total" list.
def totalOrbits(current):
    for orbit in objects_p1[current]:
        total[current] += 1
        totalOrbits(orbit)
        total[current] += total[orbit]

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    # This is the graph of the problem. I made separate ones since
    # part one doesn't need backtracking.
    objects_p1 = defaultdict(list)
    objects_p2 = defaultdict(list)
    # Dictionary with each node and their respective child count.
    total = {}
    # Use in part two tell if a node have been visited before.
    visited = {}

    for line in f:
        line = line.rstrip('\n')
        name, orbit = line.split(")")
        # Make sure to list every nodes.
        total[name] = 0
        total[orbit] = 0
        # Same here
        visited[name] = False
        visited[orbit] = False
        # Only the parents node in part1.
        objects_p1[name].append(orbit)
        # Parent to child vertex and child to parent
        objects_p2[name].append(orbit)
        objects_p2[orbit].append(name)

# PART ONE
totalOrbits("COM")
print("Total number of orbits:", sum(total.values()))

# PART TWO
path = []
# Pass the parent nodes to the function.
# We want to calculate the number of step between those two,
# not directly SANTA an YOU.
pathBetween(objects_p2["YOU"][0], objects_p2["SAN"][0], path)
