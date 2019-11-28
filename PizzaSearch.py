from AStar import aStarSearch, calculateHeuristic
from typing import *
from Graph import Graph, Node, Edge

def pizzaSearch(graph: Graph, pizzeria: Node, edges: List[Edge]) -> List[Node]:
    path = []
    currentCost = 0
    toVisit = edges
    currentNode = pizzeria

    while (len(toVisit) > 0):
        closestEdge = getClosest(pizzeria, toVisit)
        nodeA = closestEdge.nodeA
        nodeB = closestEdge.nodeB
        currentGoal = nodeA
        nodeAfterGoal = nodeB
        if (calculateHeuristic(currentNode, nodeA) > calculateHeuristic(currentNode, nodeB)):
            currentGoal = nodeB
            nodeAfterGoal = nodeA
        currentPath = aStarSearch(graph, currentNode, currentGoal)
        if currentPath[-2] != nodeAfterGoal:
            currentPath.append(nodeAfterGoal)
        
        toVisit = removeVisitedEdges(currentPath, toVisit)
        path.append(currentPath)

    if  currentNode != pizzeria:
        path.append(aStarSearch(currentNode, pizzeria))

    return path


def removeVisitedEdges(path: List[Node], toVisit: List[Edge]):
    ret: List[Edge] = toVisit
    int i = 0
    while(i+1 < len(path)):
        val1 = path[i]
        val2 = path[i+1]
        for e in ret:
            if (e.nodeA.nodeId == val1.nodeId and e.nodeB.nodeId == val2.nodeId or e.nodeA.nodeId == val2.nodeId and e.nodeB.nodeId == val1.nodeId):
                ret.remove(e)
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
    return seclosestEdge