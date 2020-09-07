from Instance import Instance
import copy

class Node():
    def __init__(self, value):
        self.__path = value
        self.__weight = 0
        self.__instance = None
    
    def __repr__(self):
        return ("{value}, {weight}").format(value = self.__path, weight = self.__weight)
    
    def setInstance(self, instance):
        self.__instance = instance
    
    def instance(self):
        return self.__instance

    def path(self):
        return self.__path
    
    def listKeys(self):
        keys = []
        for elem in self.__path:
            if elem.islower():
                keys.append(elem)
        return keys

    def weight(self):
        path = self.__path
        weight = 0
        instance = self.__instance

        if len(path) > 1:
            instance.addSteps(instance.nbStepTo(path[0], instance.position()))
            instance.toggleFound()

        for c in path[1:] if len(path) > 1 else path:
            weight += instance.nbStepTo(c, instance.position())
            instance.toggleFound()

        self.__weight = weight
        return weight


positions = {}
def createGraphFromString(string):
    graph = []
    line = []
    x, y = 0, 0
    for character in string:
        if character == '\n':
            x += 1
            y = 0
            graph.append(line[:])
            line = []
        else:
            if character.isalpha():
                positions[character] = (x, y)
            y += 1
            line.append(character)

    return graph


def generateAllNodesToVisit(paths, keys=[]):
    nodes = []

    for p in paths:
        truncatedPaths = truncatePath(p, keys)
        
        if len(p) == 1:
            nodes.append(Node("".join(p)))

        for tp in truncatedPaths:
            if tp not in nodes:
                nodes.append(Node("".join(tp)))

    return nodes


def truncatePath(path, keys):
        paths = []
        visited = []
        for elem in path:
            visited.append(elem)

            if len(visited) > 1 and elem.isupper() and validatePath(visited, keys):

                paths.append(visited[:])
                break
            elif elem.isupper():
                break

        return paths


def validatePath(path, keys):
    visited = []

    if len(path) == 0:
        return False

    for elem in path:
        visited.append(elem)
        if elem.isupper():
            if not elem.lower() in keys and not elem.lower() in visited:
                return False
            
    return True


def searchAllPaths(currentInstance):
        nodes = generateAllNodesToVisit(currentInstance.generateAllPossiblePath(), currentInstance.keys())
        total = []
        visited = {}

        for n in nodes:
            newInstance = copy.deepcopy(currentInstance)
            newInstance.keyFound(n.listKeys())
            n.setInstance(newInstance)

        while nodes:
            # Add weight
            j = nodes.pop()
            instance = j.instance()
            w = j.weight()
            instance.addSteps(w)
            visited[j.path()] = w
            instance.updateTokens()

            # generate new path
            newNodes = generateAllNodesToVisit(instance.generateAllPossiblePath(), instance.keys())
            
            if  newNodes:
                for n in newNodes:
                    path = n.path()
                    if path not in visited:
                        instance2 = copy.deepcopy(instance)
                        instance2.keyFound(n.listKeys())
                        n.setInstance(instance2)
                        nodes.append(n) 
                    else:
                        instance.addSteps(instance.nbStepTo(path[0], instance.position()))
                        instance.addSteps(visited[path])
                        print(positions[path[-1]])
                        instance.setCurrentPosition(positions[path[-1]])
            else:
                total.append(instance.nbSteps())
    
        print(total)
    

if __name__ == "__main__":
        graph = createGraphFromString("#################\n#i.G..c...e..H.p#\n########.########\n#j.A..b...f..D.o#\n########@########\n#k.E..a...g..B.n#\n########.#########l.F..d...h..C.m#\n#################\n")
        instance = Instance(graph)
        instance.updateTokens()
        searchAllPaths(instance)
    

