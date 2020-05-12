from math import gcd


DIMENSIONS = 3
NUMBER_OF_STEPS = 1000

# Part 1 functions
def step(moons, nbOfSteps):
    while nbOfSteps > 0:
        for m in moons:
            for other in moons:
                m.changeVelocity(other)
        nbOfSteps -= 1
        for m in moons:
            m.updatePosition()

def separateAxis(moons):
    result = []
    for i in range(DIMENSIONS):
        axis = []
        for m in moons:
            axis.append(Moon(m.position[i], 0))
        result.append(axis)
    return result

def totalEnergy(moons):
    total = 0
    for m in moons:
        total += m.energy()
    return total

# Part 2 functions
def repeatAfter(moons):
    # Here is my marvelous way to snapshot my list.
    comparator = [Moon(moons[0].position, 0), 
                 Moon(moons[1].position, 0), 
                 Moon(moons[2].position, 0) , 
                 Moon(moons[3].position, 0)]
    repeated = False
    i = 1

    while not repeated:
        for m in moons:
                for other in moons:
                    m.changeVelocityForOne(other)
        for m in moons:
            m.updateOnePosition()
            
        i += 1
        if moons == comparator:
            repeated = True
    return i
            
def allSystemRepeatAfter(moons):
    cycles = []
    # For each sets of moons, find the cycle of x, y and z.
    for m in moons:
        cycles.append(repeatAfter(m))

    # Found on stack overflow by user Ananay Mital
    lcm = cycles[0]
    for i in cycles[1:]:
        lcm = int(lcm*i/gcd(lcm, i))
    return lcm


# I initially created this class for dealing with 3 dimensions. I adapted it
# to be able to take only one dimension.
class Moon:
    def __init__(self, position, velocity=[0,0,0]):
        self.position = position
        if type(velocity) is list:
            self.velocity = velocity[:]
        else:
            self.velocity = velocity
    
    # No need to check the velocity here, the result will be valid.
    def __eq__(self, other):
        return self.position == other.position
    
    # Useful when debugging.
    def __repr__(self):
        return repr(self.position)

    # Here are all the behavior described in the problem.
    def changeVelocity(self, other):
        for i in range(DIMENSIONS):
            if self.position[i] > other.position[i]:
                self.velocity[i] -= 1
            elif self.position[i] < other.position[i]:
                self.velocity[i] += 1

    def updatePosition(self):
       for i in range(DIMENSIONS):
            self.position[i] += self.velocity[i]
    
    def changeVelocityForOne(self, other):
        if self.position > other.position:
            self.velocity -= 1
        elif self.position < other.position:
            self.velocity += 1

    def updateOnePosition(self):
        self.position += self.velocity
    
    def energy(self):
        p = map(abs, self.position)
        v = map(abs, self.velocity)
        return sum(p) * sum(v)


if __name__ == '__main__': 

    # Part 1
    io = Moon([13, -13, -2])
    europa = Moon([16, 2, -15])
    ganymede = Moon([7, -18, -12])
    callisto = Moon([-3, -8, -8])
    
    moons = [io, europa, ganymede, callisto]
    step(moons, NUMBER_OF_STEPS)
    print("Energy after", NUMBER_OF_STEPS,"steps:", totalEnergy(moons))

    # Part 2
    io = Moon([13, -13, -2])
    europa = Moon([16, 2, -15])
    ganymede = Moon([7, -18, -12])
    callisto = Moon([-3, -8, -8])
    
    # First separate each axis in their own list.
    moons2 = separateAxis([io, europa, ganymede, callisto])
    print("The moons cycle after:", allSystemRepeatAfter(moons2), "steps")
