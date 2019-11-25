import math
from typing import *


class Neighbour:
    def __init__(self, nodeId: int, distance: float):
        self.nodeId = nodeId
        self.distance = distance

class Node:
    nodeId: int
    neighbours: List[Neighbour] = []
    x: float = 0
    y: float = 0

    def __init__(self, nodeId: int, x: float, y: float, neighbours: List[Neighbour] = []):
        self.nodeId = nodeId
        self.x = x
        self.y = y
        self.neighbours = neighbours

    def addNeighbour(self, neighbour, distance: float):
        self.neighbours.append(Neighbour(neighbour.nodeId, distance))


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
        self.nodes[nodeA.nodeId].addNeighbour(self.nodes[nodeB.nodeId], dist)
        self.nodes[nodeB.nodeId].addNeighbour(self.nodes[nodeA.nodeId], dist)
        self.edges.append(Edge(nodeA.nodeId, nodeB.nodeId, dist))

    def getNode(self, nodeId: int) -> Node:
        return self.nodes[nodeId]


def calculateDistance(nodeA: Node, nodeB: Node) -> float:
    distX = (nodeA.x - nodeB.x)
    distY = (nodeA.y - nodeB.y)
    return math.sqrt((distX * distX) + (distY * distY))


n1 = Node(0, 1, 1, [])
n2 = Node(1, 4, 4, [])
n3 = Node(2, 15, 10, [])
n4 = Node(3, 12, 10, [])

graph = Graph()

graph.addNode(n1)
graph.addNode(n2)
graph.addNode(n3)
graph.addNode(n4)

graph.addEdge(n1, n2, 3)
graph.addEdge(n1, n3, 16)
graph.addEdge(n3, n4, 4)

print(graph.getNode(n1.nodeId).neighbours)
