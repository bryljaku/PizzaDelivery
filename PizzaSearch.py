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
            nodeA = graph.getNodeByID(closestEdge.nodeA)
            nodeB = graph.getNodeByID(closestEdge.nodeB)
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
    result: List[Edge] = toVisit
    i = 0
    while(i+1 < len(path)):
        val1 = path[i]
        val2 = path[i+1]
        if (val2 is None or val1 is None):
            break
        for e in result:
            if (e.nodeA == val1.nodeId and e.nodeB == val2.nodeId or e.nodeA == val2.nodeId and e.nodeB == val1.nodeId):
                result.remove(e)
        i += 1
    return result



def getClosestEdge(graph: Graph, current: Node, toVisit: List[Edge]):
    closestEdge = None
    currentDist = 99999
    for edge in toVisit:
        nodeA = graph.nodes[edge.nodeA]
        nodeB = graph.nodes[edge.nodeB]
        a_heur = calculateHeuristic(current, nodeA)
        b_heur = calculateHeuristic(current, nodeB)
        if (currentDist > min(a_heur, b_heur)):
            closestEdge = edge
            currentDist = min(a_heur, b_heur)
    return closestEdge
