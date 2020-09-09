from Instance import Instance
import copy

class Node():
    def __init__(self, path, instance=None):
        self.__path = path
        self.__weight = 0
        self.__instance = instance
    
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


def createGraphFromString(string):
    graph = []
    line = []
    x, y = 0, 0
    for character in string:
        if character == '\n':
            graph.append(line[:])
            line = []
        else:
            line.append(character)

    return graph


def generateAllNodes(paths, instance=None):
    nodes = []

    for p in paths:
        nodes.append(Node("".join(p), instance))

    return nodes


def searchAllPaths(currentInstance):
        totals = []
        visited = {}

        # A node represent a path, not a single point. Each nodes have its own instance.
        # Example ['aA']
        nodes = generateAllNodes(currentInstance.generateAllPossiblePath(), currentInstance)
  
        for n in nodes:
            newInstance = copy.deepcopy(currentInstance)
            # TODO: could be done when generating path
            newInstance.keyFound(n.listKeys())
        
        # TODO: function!
        while nodes:

            no = nodes.pop()
            instance = no.instance()
            w = no.weight()

            # Add weight ['aA'] => 4
            # The instance also count the number of step required to reach
            # the first letter => 2.
            instance.addSteps(w)
            if len(no.path()) > 2:
                # TODO: visited node should be added recursively
                visited[no.path()] = w
            instance.updateTokens()

            # From the current node, generate all possible path.
            # Example: ['b']
            newNodes = generateAllNodes(instance.generateAllPossiblePath())
            
            if  newNodes:
                for n in newNodes:
                    path = n.path()
                    # 
                    if path not in visited:
                        # TODO: function!
                        instance2 = copy.deepcopy(instance)
                        instance2.keyFound(n.listKeys())
                        n.setInstance(instance2)
                        nodes.append(n) 
                    else:
                        # If the weight is already computed, use the stored value.
                        # Still have to process the number of step to get to the first position.
                        instance.addSteps(instance.nbStepTo(path[0], instance.position()))
                        instance.addSteps(visited[path])
                        instance.setCurrentPosition(instance.getPostionFromValue(path[-1]))

            if not newNodes or not nodes:
                totals.append(instance.nbSteps())
                
    
        print(totals)
    

if __name__ == "__main__":
        # Graph example:#########
                        #b.A.@.a#
                        #########

        graph = createGraphFromString("#########\n#b.A.@.a#\n#########\n")
        # An instance contains useful information of a search
        # - Graph
        # - Current Position
        # - Key found
        # - Number of step taken
        # - All available keys and doors for the current position
        instance = Instance(graph)
        
        # Find all available keys and doors and store it in the first instance
        instance.updateTokens()
        instance.listPositions()
        searchAllPaths(instance)


    

