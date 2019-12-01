from AStar import *
from Graph import *
from PizzaSearch import *

bipartiteGraph = Graph()
bipartiteGraphNodes = [Node(0, 5, 5), Node(1, 9, 7), Node(2, 5, 7), Node(3, 9, 5), Node(4, 5, 3), Node(5, 9, 3)]
bipartiteGraphEdges = [Edge(0, 1, 6), Edge(0, 3, 10), Edge(2, 3, 7), Edge(3, 4, 12), Edge(4, 5, 5)]

for node in bipartiteGraphNodes:
    bipartiteGraph.addNode(node)
for edge in bipartiteGraphEdges:
    bipartiteGraph.addEdge(edge)

pizzaDeliveryList = [bipartiteGraphEdges[2], bipartiteGraphEdges[4]]
pizzeria = bipartiteGraphNodes[0]

print('id  cost')
for node in bipartiteGraph.nodes.values():
    for key, value in bipartiteGraph.getNodeByID(node.nodeId).neighbors.items():
        print(str(node.nodeId) + ' -> ' + str(key) + ' = ' + str(value.distance))

# ret = aStarSearch(graph, graph.getNodeByID(n1.nodeId), graph.getNodeByID(n4.nodeId))
ret = pizzaDelivery(bipartiteGraph, pizzeria, pizzaDeliveryList)

for node_list in ret:
    print("Path part: ")
    for node in node_list:
        print(node.nodeId)

