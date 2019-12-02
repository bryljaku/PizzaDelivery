from AStar import *
from Graph import *
from PizzaDelivery import *

'''
data sets for testing:

bipartite graph:
nodes = [Node(0, 5, 5), Node(1, 9, 7), Node(2, 5, 7), Node(3, 9, 5), Node(4, 5, 3), Node(5, 9, 3)]
edges = [Edge(0, 1, 6), Edge(0, 3, 10), Edge(2, 3, 7), Edge(3, 4, 12), Edge(4, 5, 5)]
pizzaDeliveryList = [testedGraphEdges[2], testedGraphEdges[4]]

bipartite graph with beltway:
nodes = [Node(0, 5, 5), Node(1, 9, 7), Node(2, 5, 7), Node(3, 9, 5), Node(4, 5, 3), Node(5, 9, 3)]
edges = [Edge(0, 1, 6), Edge(0, 3, 10), Edge(2, 3, 7), Edge(3, 4, 12), Edge(4, 5, 5), Edge(1, 4, 12),
         Edge(2, 4, 4), Edge(2, 1, 4), Edge(1, 5, 4)]
pizzaDeliveryList = [testedGraphEdges[2], testedGraphEdges[4], testedGraphEdges[5]]  # additional long edge to visit,
                                                                          # check if algorithm traverses through beltway

tree:
nodes = [Node(0, 20, 20), Node(1, 15, 15), Node(2, 20, 17), Node(3, 25, 10), Node(4, 5, 10), Node(5, 9, 7),
         Node(6, 22, 3), Node(7, 25, 5)]
edges = [Edge(0, 1, 14), Edge(0, 2, 6), Edge(0, 3, 15), Edge(3, 6, 10), Edge(3, 7, 5), Edge(1, 4, 13),
         Edge(1, 5, 10)]
pizzaDeliveryList = [testedGraphEdges[1], testedGraphEdges[5], testedGraphEdges[3]]  # delivery to leaves

polygon-like graph:
nodes = [Node(0, 0, 0), Node(1, 4, 3), Node(2, 7, 9), Node(3, 12, 6), Node(4, 5, 0)]
edges = [Edge(0, 1, 7), Edge(0, 4, 8), Edge(1, 2, 7), Edge(1, 3, 10), Edge(1, 4, 4), Edge(2, 3, 6),
                    Edge(3, 4, 10)]
pizzaDeliveryList = [testedGraphEdges[1], testedGraphEdges[4], testedGraphEdges[5]]

no delivery: only 0 vertex as a path
empty graph: error at least one vertex
'''

testedGraph = Graph()
testedGraphNodes = [Node(0, 0, 0), Node(1, 4, 3), Node(2, 7, 9), Node(3, 12, 6), Node(4, 5, 0)]
testedGraphEdges = [Edge(0, 1, 7), Edge(0, 4, 8), Edge(1, 2, 7), Edge(1, 3, 10), Edge(1, 4, 4), Edge(2, 3, 6),
                    Edge(3, 4, 10)]

for node in testedGraphNodes:
    testedGraph.addNode(node)
for edge in testedGraphEdges:
    testedGraph.addEdge(edge)

pizzaDeliveryList = [testedGraphEdges[1], testedGraphEdges[4], testedGraphEdges[5]]
pizzeria = testedGraphNodes[0]

print('id  cost')
for node in testedGraph.nodes.values():
    for key, value in testedGraph.getNodeByID(node.nodeId).neighbors.items():
        print(str(node.nodeId) + ' -> ' + str(key) + ' = ' + str(value.distance))

def pathMerge(pathsList):
    for i in range(0, len(pathsList) - 1):
        if pathsList[i][-1] == pathsList[i+1][0]:  # in order not to duplicate vertices
            pathsList[i+1].pop(0)
    flatList = []
    for sublist in pathsList:
        for element in sublist:
            flatList.append(element)
    return flatList


def solvePizzaProblem(graph, start, deliveryList):
    ret = pizzaDelivery(graph, start, deliveryList)
    return pathMerge(ret)


fullPath = solvePizzaProblem(testedGraph, pizzeria, pizzaDeliveryList)
print("\n" + "Full path: ")
for node in fullPath:
    print(node.nodeId)
