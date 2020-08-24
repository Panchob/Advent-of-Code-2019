import itertools

RIGHT = (0, 1)
LEFT = (0, -1)
UP = (1, 0)
DOWN = (-1, 0)

class Instance():
    def __init__(self, graph, position):
        self.__graph = graph[:]
        self.__position = position
        self.__nbSteps = 0
        # Everything that "@" has access to.
        self.__tokens = []


    def getPosition(self):
        return self.__position
    
    def getValue(self):
        x, y = self.__position
        return self.__graph[x][y]

    def setEmptyAt(self, position):
        x, y = position
        graph[x][y] = "." 

    def listAvailableElementsFromPosition(direction=None):
        x,y = self.position
        keysAndDoors = []
        current = self.graph[x][y]

        if current != '#':
        
            if current.isalpha():
                keysAndDoors.append(current)
                if current.isupper():
                    # Consider close doors as wall. (duh)
                    return keysAndDoors

            for d in getDirectionsWithoutBacktracking(direction):
                res = listAvailableElementsFromPosition(graph, (x + d[0], y + d[1]), d)
                if res:
                    keysAndDoors.extend(res)

        self.__token = keysAndDoors

    def generateAllPossiblePath():
        return itertools.permutations(self.__tokens)

    def getCurrentPosition():   
            for x in range(1, len(self.__graph) - 1):
                for y in range(1, len(self.__graph[0]) - 1):
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