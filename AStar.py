import math

class Node:
    neighbours = []
    x = 0
    y = 0

    def __init__(self, x, y, neighbours=[]):
        self.x = x
        self.y = y
        self.neighbours = neighbours
class Edge:
    def __init__(self, nodeA, nodeB, length):
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.length = length


def calculateDistance(nodeA: Node, nodeB: Node) -> int:
    distX = (nodeA.x-nodeB.x)
    distY = (nodeA.y-nodeB.y)
    return math.sqrt((distX*distX)+(distY*distY))

class State:
    def __init__(self, path=[], cost=0, heuristic=0):
        self.path = path
        self.cost = cost
        self.heuristic = heuristic

    def getNextStates(self):
        states = []
        for node in self.path[-1].neighbours:
                if node in self.path:
                    continue
                p = self.path.append(node)
                states.append(State(p, self.cost + 5, node.heuristicToPizzeria))  # todo correct cost calulation


def findCheapestInArrayOfStates(arr):
    cheapest = arr[0]
    for s in arr:
        if s.cost + s.heuristic < cheapest.cost + cheapest.heuristic:
            cheapest = s
    return cheapest


def search(start, end):
    """
    start - start node of a graph
    end - end node of a graph

    returns a path of nodes
    """
    toVisitStates = [State([start], 0, 10)]
    while len(toVisitStates) > 0:
        currentState = findCheapestInArrayOfStates(toVisitStates)
        if end in currentState.path:
            return currentState
        toVisitStates.pop()
        toVisitStates.append(currentState.getNextStates)
    print("given graph is corrupted")
