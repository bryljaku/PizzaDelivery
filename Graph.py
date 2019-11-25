import math
from typing import *


class Neighbor:
    def __init__(self, nodeId: int, distance: float):
        self.nodeId = nodeId
        self.distance = distance


class Node:
    nodeId: int
    neighbors = {}
    x: float = 0
    y: float = 0

    def __init__(self, nodeId: int, x: float, y: float):
        self.nodeId = nodeId
        self.x = x
        self.y = y

    def addNeighbor(self, neighbor, distance: float):
        self.neighbors[neighbor.nodeId] = Neighbor(neighbor.nodeId, distance)


class Edge:
    def __init__(self, nodeA: int, nodeB: int, length: float):
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.length = length


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def addNode(self, node: Node):
        self.nodes[node.nodeId] = node

    def addEdge(self, nodeA: Node, nodeB: Node, dist: float):
        self.nodes[nodeA.nodeId].addNeighbor(self.nodes[nodeB.nodeId], dist)
        self.nodes[nodeB.nodeId].addNeighbor(self.nodes[nodeA.nodeId], dist)
        self.edges.append(Edge(nodeA.nodeId, nodeB.nodeId, dist))

    def getNode(self, nodeId: int) -> Node:
        return self.nodes[nodeId]

    def cost(self, nodeA: Node, nodeB: Node):
        return self.nodes[nodeA.nodeId].neighbors[nodeB.nodeId].distance

    def neighbors(self, node: Node):
        return self.nodes[node.nodeId].neighbors
