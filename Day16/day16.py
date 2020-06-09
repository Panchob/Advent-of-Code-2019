from itertools import cycle, repeat
import os
import sys

PATTERN = [0, 1, 0, -1]

# TODO: This will not be fast enough for part 2. I have to tweak the perf
# on this calculation.
def phase(input):
    out = []
    for j in range(1, len(input) + 1):
        pos = 1
        result = 0
        pattern = []
       
        for num in PATTERN:
            for i in range(j):
                pattern.append(num)

        c = cycle(pattern)
        next(c)
        for i in input:
            current = next(c)
            result += i * current
        
        result = abs(result) % 10
        out.append(result)
    return out

def multiphasing(input, nb):
    out = input
    for i in range(nb):
        out = phase(out)
    string = [str(l) for l in out[0:8]]
    r = ''.join(string)
    return r

if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        str = f.read()
        signal = [int(c) for c in str]

        print(multiphasing(signal, 100))