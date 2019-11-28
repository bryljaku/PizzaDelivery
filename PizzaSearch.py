from AStar import aStarSearch, calculateHeuristic
from typing import *
from Graph import Graph, Node, Edge

def pizzaSearch(graph: Graph, pizzeria: Node, edges: List[Edge]) -> List[Node]:
    path = []
    cost = 0
    toVisit = edges
    currentNode = pizzeria

    while (len(toVisit) > 0):
        closestEdge = getClosestEdge(graph, pizzeria, toVisit)
        if closestEdge is not None:
            nodeA = graph.getNode(closestEdge.nodeA)
            nodeB = graph.getNode(closestEdge.nodeB)
            currentGoal = nodeA
            nodeAfterGoal = nodeB
            if (calculateHeuristic(currentNode, nodeA) > calculateHeuristic(currentNode, nodeB)):
                currentGoal = nodeB
                nodeAfterGoal = nodeA
            currentPath, currentCost = aStarSearch(graph, currentNode, currentGoal)
            if currentPath[-2] != nodeAfterGoal:
                currentPath.append(nodeAfterGoal)
            
            toVisit = removeVisitedEdges(currentPath, toVisit)
            path.append(currentPath)
            currentNode = currentPath[-1]
        else:
            currentPath, currentCost = aStarSearch(currentNode, pizzeria)
            path.append(currentPath)

    return path


def removeVisitedEdges(path: List[Node], toVisit: List[Edge]):
    ret: List[Edge] = toVisit
    i = 0
    while(i+1 < len(path)):
        val1 = path[i]
        val2 = path[i+1]
        if (val2 is None or val1 is None):
            break
        for e in ret:
            if (e.nodeA == val1.nodeId and e.nodeB == val2.nodeId or e.nodeA == val2.nodeId and e.nodeB == val1.nodeId):
                ret.remove(e)
        i += 1
    return ret



def getClosestEdge(graph: Graph, current: Node, toVisit: List[Edge]):
    closestEdge = None
    currentDist = 99999
    for edge in toVisit:
        nodeA = graph.nodes[edge.nodeA]
        nodeB = graph.nodes[edge.nodeB]
        a = calculateHeuristic(current, nodeA)
        b = calculateHeuristic(current, nodeA)
        if (currentDist > min(a, b)):
            closestEdge = edge
            currentDist = min(a, b)
    return closestEdge
