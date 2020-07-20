import os
import sys

FIRST_PARAM = 0
SECOND_PARAM = 1
THIRD_PARAM = 2

def positions(l, i, relative_base):
    # Append in the same order as the values in l. By using
    # modulo, if the length of the instruction is smaller than
    # the number of values, 0 is returned.
    modes = []
    modes.append((l[i]//100) % 10)
    modes.append((l[i]//1000) % 10)
    modes.append((l[i]//10000) % 10)

    # Start at one since the current index is currently on
    # the instruction and not the first value. I reuse the same array
    # here to store the position (immediate or not) of the values.
    # Ex: j is 0 and position is 1 for [1002, 4, 3, 33]
    # modes = [0*][1][0]
    # l = ... [1002][4*][3][33] ... with * being the current index.
    position = 1
    for j in range(len(modes)):
        if i + position == len(l):
            break
        # Position mode
        if modes[j] == 0:
            modes[j] = l[i + position]
        # Immediate mode
        elif modes[j] == 1:
            modes[j] = i + position
        # Relative base mode
        else:
            modes[j] = relative_base + l[i + position]

        position += 1

    return modes

def parseIntcode(file):
    with open(os.path.join(sys.path[0], file), "r") as f:
        code =list(map(int, f.read().split(",")))
        padding =  [0] * 10000
        return code + padding


class Intcode:
    def __init__(self, file):
        self.memory = parseIntcode(file)[:]
        self.input = None
        self.position = 0
        self.stopped = False
        self.waiting = False
        self.relative_base = 0
        
    def run(self, input=None):
        if input is None:
            input = self.input
            
        i = self.position
        memory = self.memory
        increment = 0
        
        while i < len(memory):
            instruction = memory[i] % 100
            if instruction == 99:
                self.stopped = True
                #FIX: this is a problem for certain days.
                return 10

            instruction = instruction % 10
            pos = positions(memory, i, self.relative_base)

            # 1 - addition
            if instruction == 1:
                memory[pos[THIRD_PARAM]] = memory[pos[FIRST_PARAM]] + memory[pos[SECOND_PARAM]]
                increment = 4
            # 2 - multiplication
            elif instruction == 2:
                memory[pos[THIRD_PARAM]] = memory[pos[FIRST_PARAM]] * memory[pos[SECOND_PARAM]]
                increment = 4
            # 3 - Store input value
            elif instruction == 3:
                if input is None:
                    self.position = i
                    self.waiting = True
                    break
                else:
                    self.waiting = False

                memory[pos[FIRST_PARAM]] = input
                input = None

                increment = 2
            # 4 - Output values
            elif instruction == 4:
                self.position = i + 2
                return(memory[pos[FIRST_PARAM]])
                
            # 5 - Jump if true
            elif instruction == 5:
                if memory[pos[FIRST_PARAM]] != 0:
                    i = memory[pos[SECOND_PARAM]]
                    increment = 0
                else:
                    increment = 3
            # 6 - Jump if false
            elif instruction == 6:
                if memory[pos[FIRST_PARAM]] == 0:
                    i = memory[pos[SECOND_PARAM]]
                    increment = 0
                else:
                    increment = 3
            # 7 - Less than
            elif instruction == 7:
                if memory[pos[FIRST_PARAM]] < memory[pos[SECOND_PARAM]]:
                    memory[pos[THIRD_PARAM]] = 1
                else:
                    memory[pos[THIRD_PARAM]] = 0
                increment = 4
            # 8 - Equals
            elif instruction == 8:
                if memory[pos[FIRST_PARAM]] == memory[pos[SECOND_PARAM]]:
                    memory[pos[THIRD_PARAM]] = 1
                else:
                    memory[pos[THIRD_PARAM]] = 0
                increment = 4
            # 9 - Adjust the relative base
            elif instruction == 9:
                self.relative_base += memory[pos[FIRST_PARAM]]
                increment = 2
            # Bad instruction
            else:
                break
            i += increment
        
    def setInput(self, input):
        self.input = input
        self.waiting = False
    
    def getOutput(self):
        out = []
        while( not self.waiting and not self.stopped):
            out.append(self.run())
        # All the value except the last since it will always be None
        return out[:-1]
            




