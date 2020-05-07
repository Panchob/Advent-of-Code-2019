with open(r"C:\Users\franc\OneDrive\Documents\Advent\2019\Day5\input.txt", "r") as f:

    l = f.read().split(",")
    l = list(map(int, l))
    i = 0
    instruction = 0
    inc = 4
    phase = True
    #l = [102,3,4,4,33]
    #l = [1001,1,1,1]
    #l = [1102, 72, 20, 10, 1001, 10, -1440, 10, 4, 10, 0]



    while i < len(l):
        

        instruction = l[i]   %10
        mode = []
        mode.append((l[i]//100)  %10)
        mode.append((l[i]//1000)  %10)
        mode.append((l[i]//10000)  %10)
        
        j = 1
        if instruction == 9:
            break
        for m in range(len(mode)):
            if mode[m] == 0:
                mode[m] = l[i + j]
            else:
                mode[m] = i + j
            j += 1 

        print(instruction, mode)
        if instruction == 1:
            l[mode[2]] = l[mode[0]] + l[mode[1]] 
            inc = 4
        elif instruction == 2:
            l[mode[2]] = l[mode[0]] * l[mode[1]] 
            inc = 4
        elif instruction == 3:
            if phase:
                l[l [i + 1]] = 1
                phase = False
            else:
                l[l [i + 1]] = 210
                
            inc = 2
        elif instruction == 4:
            print(l[mode[0]])
            inc = 2
        elif instruction == 5:
            if(l[mode[0]] != 0):
                i = l[mode[1]]
                inc = 0
            else:
                inc = 3
        elif instruction == 6:
            if(l[mode[0]] == 0):
                i = l[mode[1]]
                inc = 0
            else:
                inc = 3
        elif instruction == 7:
            if (l[mode[0]] < l[mode[1]]):
                l[mode[2]] = 1
            else:
                l[mode[2]] = 0
            inc = 4
        elif instruction == 8:
            if (l[mode[0]] == l[mode[1]]):
                l[mode[2]] = 1
            else:
                 l[mode[2]] = 0
            inc = 4
        else:
            break
        i += inc
print(l)
    
