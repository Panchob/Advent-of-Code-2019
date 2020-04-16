import array
import sys
import os


def compile(l):
    i = 0
    while i < len(l):
        if  l[i] == 1:
            l[l[i + 3]] =  l[l[i + 1]] + l[l[i + 2]]
        elif l[i] == 2:
            l[l[i + 3]] =  l[l[i + 1]] * l[l[i + 2]]
        else:
            break
        i += 4

    return l


with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    l = list(map(int, f.read().split(",")))
    print(compile(l)[0])