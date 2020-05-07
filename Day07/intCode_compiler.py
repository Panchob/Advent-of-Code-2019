
FIRST_PARAM = 0
SECOND_PARAM = 1
THIRD_PARAM = 2

def positions(l, i):
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
        else:
            modes[j] = i + position
        position += 1

    return modes

class Intcode:
    def __init__(self, intCode):
        self.code = intCode[:]
        self.position = 0
        self.stopped = False
        
    def run(self, input):
        i = self.position
        increment = 0
        l = self.code
        
        while i < len(l):
            instruction = l[i] % 10
            # 9 - End (Will change if I have to really use 9)
            if instruction == 9:
                self.stopped = True
                return input

            pos = positions(l, i)

            # 1 - addition
            if instruction == 1:
                l[pos[THIRD_PARAM]] = l[pos[FIRST_PARAM]] + l[pos[SECOND_PARAM]]
                increment = 4
            # 2 - multiplication
            elif instruction == 2:
                l[pos[THIRD_PARAM]] = l[pos[FIRST_PARAM]] * l[pos[SECOND_PARAM]]
                increment = 4
            # 3 - Store input value
            elif instruction == 3:
                if input is None:
                    self.position = i
                    break

                l[pos[FIRST_PARAM]] = input
                input = None
                increment = 2
            # 4 - output value
            elif instruction == 4:
                self.position = i + 2
                return(l[pos[FIRST_PARAM]])

            # 5 - Jump if true
            elif instruction == 5:
                if l[pos[FIRST_PARAM]] != 0:
                    i = l[pos[SECOND_PARAM]]
                    increment = 0
                else:
                    increment = 3
            # 6 - Jump if false
            elif instruction == 6:
                if l[pos[FIRST_PARAM]] == 0:
                    i = l[pos[SECOND_PARAM]]
                    increment = 0
                else:
                    increment = 3
            # 7 - Less than
            elif instruction == 7:
                if l[pos[FIRST_PARAM]] < l[pos[SECOND_PARAM]]:
                    l[pos[THIRD_PARAM]] = 1
                else:
                    l[pos[THIRD_PARAM]] = 0
                increment = 4
            # 8 - Equals
            elif instruction == 8:
                if l[pos[FIRST_PARAM]] == l[pos[SECOND_PARAM]]:
                    l[pos[THIRD_PARAM]] = 1
                else:
                    l[pos[THIRD_PARAM]] = 0
                increment = 4
            # Bad instruction
            else:
                break
            i += increment




