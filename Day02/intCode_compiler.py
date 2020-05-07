
import sys
import os


def compile(l):
    i = 0

    while i < len(l):
        instruction = l[i]

        # 99 - End
        if instruction == 99:
            break
        # The two values to use.
        v1 = l[i + 1]
        v2 = l[i + 2]
        # Where to store the result.
        r = l[i + 3]

        # 1 - addition
        if  instruction == 1:
            l[r] =  l[v1] + l[v2]
        # 2 - multiplication
        elif l[i] == 2:
            l[r] =  l[v1] * l[v2]
        else:
            break
        # increment by 4 to get to the next instruction
        i += 4

    return l


with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    l = list(map(int, f.read().split(",")))
    print(compile(l)[0])