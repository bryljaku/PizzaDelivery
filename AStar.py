class Node:
    neighbours = []
    heuristicToPizzeria = 0

    def __init__(self, neighbours=[], heuristicToPizza=0):
        self.neighbours = neighbours
        self.heuristicToPizzeria = heuristicToPizza


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


def findCheapestFromArr(arr):
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
        currentState = findCheapestFromArr(toVisitStates)
        if end in currentState.path:
            return currentState
        toVisitStates.pop()
        toVisitStates.append(currentState.getNextStates)
    print("given graph is corrupted")
