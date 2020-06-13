import os
import sys
from intCode_compiler import Intcode

def listIntersection(graph):
    intersection = set()

    for node in graph:
        x, y = node
        adjacents = [(x- 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        if all(a in graph for a in adjacents):
            intersection.add((x - 1, y))
    
    return (intersection)


with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    l = f.read().split(",")
    l = list(map(int, l))
    padding =  [0] * 10000
    memory = l + padding

with open(os.path.join(sys.path[0], "output.txt"), "w") as w:
    intcode = Intcode(memory)
    w.write(" ")

    graph = set()
    x = 0
    y = 0
    while not intcode.stopped:
        num = intcode.run()
        if num == 10:
            y += 1
            x = 0
        else:
            x += 1
            if num == 35:
                graph.add((x, y))

        w.write(chr(num))
        w.write(" ")

intersections = listIntersection(graph)
alignments = [i[0] * i[1] for i in intersections]
print(intersections)
print(alignments)
print(sum(alignments))