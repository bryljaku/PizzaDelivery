from AStar import *
from Graph import *
from PizzaSearch import *
n1 = Node(0, 1, 1)
n2 = Node(1, 4, 4)
n3 = Node(2, 15, 10)
n4 = Node(3, 12, 10)

graph = Graph()

graph.addNode(n1)
graph.addNode(n2)
graph.addNode(n3)
graph.addNode(n4)

graph.addEdge(n1, n2, 3)
graph.addEdge(n1, n3, 6)
graph.addEdge(n3, n4, 4)


# print(graph.getNodeByID(n1.nodeId).neighbors)
print(n1.neighbors)
print('id  cost')
for node in graph.nodes.values():
    for key, value in graph.getNodeByID(node.nodeId).neighbors.items(): #for key, value in node.neighbors.items():
        print(str(node.nodeId) + ' -> ' + str(key) + ' = ' + str(value.distance))

# ret = aStarSearch(graph, graph.getNodeByID(n1.nodeId), graph.getNodeByID(n4.nodeId))
ret = pizzaSearch(graph, graph.nodes[n1.nodeId], [graph.edges[2]])
for a in ret:
    print
    # assert(path == 0->3->4)