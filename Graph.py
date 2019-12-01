import math
from typing import *
# from AStar import calculateHeuristic



class Neighbor:
    def __init__(self, nodeId: int, distance: float):
        self.nodeId = nodeId
        self.distance = distance

class Node:
    def __init__(self, nodeId: int, x: float, y: float):
        self.nodeId = nodeId
        self.x = x
        self.y = y
        self.neighbors: DefaultDict[(int, Neighbor)] = {}

    def __lt__(self, other):
        return self.nodeId < other.nodeId

    def __le__(self, other):
        return self.nodeId <= other.nodeId

    def __gt__(self, other):
        return self.nodeId > other.nodeId

    def __ge__(self, other):
        return self.nodeId >= other.nodeId

    def addNeighbor(self, neighbor, distance: float):
        n = Neighbor(neighbor.nodeId, distance)
        self.neighbors[neighbor.nodeId] = n


class Edge:
    def __init__(self, nodeA: int, nodeB: int, length: float):
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.length = length

class Graph:
    def __init__(self):
        self.nodes: DefaultDict[(int, Node)] = {}
        self.edges: List[Edge] = []

    def addNode(self, node: Node):
        self.nodes[node.nodeId] = node

    def createAndAddEdge(self, nodeA: Node, nodeB: Node, dist: float):
        from AStar import calculateHeuristic  # circular dependencies occured
        if not self.isDistanceCorrect(calculateHeuristic(nodeA, nodeB), dist):
            raise Exception("Incorrect distance between node " + str(nodeA.nodeId) + " and node " + str(nodeB.nodeId))
        self.nodes[nodeA.nodeId].addNeighbor(self.nodes[nodeB.nodeId], dist)
        self.nodes[nodeB.nodeId].addNeighbor(self.nodes[nodeA.nodeId], dist)
        self.edges.append(Edge(nodeA.nodeId, nodeB.nodeId, dist))

    def addEdge(self, edge: Edge):
        nodeA = self.getNodeByID(edge.nodeA)
        nodeB = self.getNodeByID(edge.nodeB)
        return self.createAndAddEdge(nodeA, nodeB, edge.length)

    def isDistanceCorrect(self, minimalDist: float, dist: float):  # to check heuristic condition
        return dist >= minimalDist

    def getNodeByID(self, nodeId: int) -> Node:
        return self.nodes[nodeId]

    def getCost(self, nodeA: Node, nodeB: Node) -> float:
        return self.nodes[nodeA.nodeId].neighbors[nodeB.nodeId].distance

    def getNeighbors(self, node: Node) -> DefaultDict[(int, Neighbor)]:
        return self.nodes[node.nodeId].neighbors
