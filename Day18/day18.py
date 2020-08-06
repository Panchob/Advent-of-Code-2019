import itertools

RIGHT = (0, 1)
LEFT = (0, -1)
UP = (1, 0)
DOWN = (-1, 0)

class Node():
    def __init__(self, value):
        self.value = value
        self.weight = 0
    
    def __repr__(self):
        return self.value
    
def createGraphFromString(string):
    graph = []
    line = []
    for character in string:
        if character == '\n':
            graph.append(line[:])
            line = []
        else:
            line.append(character)

    return graph


def getCurrentPosition(graph):
        for x in range(1, len(graph) - 1):
            for y in range(1, len(graph[0]) - 1):
                if graph[x][y] == '@':
                    return (x, y)



def getDirectionsWithoutBacktracking(lastDirection):
    directions = [RIGHT, LEFT, UP, DOWN]

    if lastDirection == RIGHT:
        directions.pop(1)
    elif lastDirection == LEFT:
        directions.pop(0)
    elif lastDirection == UP:
        directions.pop(3)
    elif lastDirection == DOWN:
        directions.pop(2)

    return directions


# List everything that "@" has access to. I'm not classifying the in keys or
# doors yet, just elements with distance from starting position and positions.
def listAvailableElementsFromPosition(graph, position, steps, direction=None):
    x,y = position
    keysAndDoors = []
    current = graph[x][y]

    if current != '#':
       
        if current.isalpha():
            keysAndDoors.append(current)
            if current.isupper():
                # Consider close doors as wall.
                return keysAndDoors

        for d in getDirectionsWithoutBacktracking(direction):
            res = listAvailableElementsFromPosition(graph, (x + d[0], y + d[1]), steps + 1, d)
            if res:
                keysAndDoors.extend(res)

    return keysAndDoors


def generateAllPossiblePath(keysAndDoors):
    return itertools.permutations(keysAndDoors)


def generateAllNodesToVisit(paths):
    nodes = []
    for p in paths:
        if validatePath(p):
            nodes.append(Node("".join(p)))
    
    return nodes


def validatePath(path):
    visited = []
    for elem in path:
        if elem.isupper():
            if not elem.lower() in visited:
                return False
        visited.append(elem)
    return True

    

if __name__ == "__main__":
    pass
    

