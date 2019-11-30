import typing
from HeapPriorityQueue import HeapPriorityQueue as PriorityQueue
from Graph import *

def calculateHeuristic(nodeA: Node, nodeB: Node) -> float:
    distX = (nodeA.x - nodeB.x)
    distY = (nodeA.y - nodeB.y)
    return math.sqrt((distX * distX) + (distY * distY))


def reconstructPath(cameFrom, goal: Node):
    path = [goal]
    curr = goal
    while curr in cameFrom.keys() and cameFrom[curr] is not None:
        curr = cameFrom[curr]
        path.append(curr)
    path.reverse()
    return path

def aStarSearch(graph: Graph, start: Node, goal: Node):
    nodesToVisit: PriorityQueue[Node] = PriorityQueue()
    nodesToVisit.put(start, 0)
    cameFrom = {}
    currentCost = {}
    cameFrom[start] = None
    currentCost[start] = 0
    
    while not nodesToVisit.empty():
        current = nodesToVisit.get()
        print(current.nodeId)
        if current == goal:
            break

        for node in graph.getNodeByID(current.nodeId).neighbors.values():  # current.neighbors.values()
            next_node = graph.getNodeByID(node.nodeId)  # = node, not node bc node is Neighbor and node is Node
            newCost = currentCost[current] + graph.getCost(current, next_node)
            if next_node not in currentCost or newCost < currentCost[next_node]:  # if cost for next_node not calculated or found cheaper path
                currentCost[next_node] = newCost
                priority = newCost + calculateHeuristic(goal, next_node)
                nodesToVisit.put(next_node, priority)
                cameFrom[next_node] = current

    return reconstructPath(cameFrom, goal), currentCost

