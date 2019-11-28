import typing
from HeapPriorityQueue import HeapPriorityQueue as PriorityQueue
from Graph import *

def calculateHeuristic(nodeA: Node, nodeB: Node) -> float:
    distX = (nodeA.x - nodeB.x)
    distY = (nodeA.y - nodeB.y)
    return math.sqrt((distX * distX) + (distY * distY))


def reconstructPath(cameFrom, goal:Node):
    path = [goal]
    curr = goal
    while cameFrom[curr] is not None:
        curr = cameFrom[curr]
        path.append(curr)
    path.reverse()
    return path

def aStarSearch(graph: Graph, start: Node, goal: Node):
    toVisit:PriorityQueue[Node] = PriorityQueue()
    toVisit.put(start, 0)
    cameFrom = {}
    currentCost = {}
    cameFrom[start] = None
    currentCost[start] = 0
    
    while not toVisit.empty():
        current = toVisit.get()
        print(current.nodeId)
        if current == goal:
            break

        for node in graph.getNode(current.nodeId).neighbors.values():
            next = graph.getNode(node.nodeId)
            newCost = currentCost[current] + graph.cost(current, next)
            if next not in currentCost or newCost < currentCost[next]:
                currentCost[next] = newCost
                priority = newCost + calculateHeuristic(goal, next)
                toVisit.put(next, priority)
                cameFrom[next] = current

    return reconstructPath(cameFrom, goal), currentCost

