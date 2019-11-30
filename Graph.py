import math
from typing import *

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

    def addEdge(self, nodeA: Node, nodeB: Node, dist: float):
        self.nodes[nodeA.nodeId].addNeighbor(self.nodes[nodeB.nodeId], dist)
        self.nodes[nodeB.nodeId].addNeighbor(self.nodes[nodeA.nodeId], dist)
        self.edges.append(Edge(nodeA.nodeId, nodeB.nodeId, dist))

    def getNodeByID(self, nodeId: int) -> Node:
        return self.nodes[nodeId]

    def getCost(self, nodeA: Node, nodeB: Node) -> float:
        return self.nodes[nodeA.nodeId].neighbors[nodeB.nodeId].distance

    def getNeighbors(self, node: Node) -> DefaultDict[(int, Neighbor)]:
        return self.nodes[node.nodeId].neighbors
