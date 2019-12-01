from AStar import *
from Graph import *
from PizzaSearch import *
# n1 = Node(0, 1, 1)
# n2 = Node(1, 4, 4)
# n3 = Node(2, 15, 10)
# n4 = Node(3, 12, 10)

# tree-like graph, cycle in one 'subtree'
n0 = Node(0, 10, 10)
n1 = Node(1, 4, 4)
n2 = Node(2, 7, 12)
n3 = Node(3, 12, 10)

graph = Graph()

# graph.addNode(n1)
# graph.addNode(n2)
# graph.addNode(n3)
# graph.addNode(n4)
graph.addNode(n0)
graph.addNode(n1)
graph.addNode(n2)
graph.addNode(n3)

# graph.addEdge(n1, n2, 3)
# graph.addEdge(n1, n3, 6)
# graph.addEdge(n3, n4, 4)
graph.addEdge(n0, n1, 10)
graph.addEdge(n0, n2, 6)
graph.addEdge(n3, n0, 2)
graph.addEdge(n2, n1, 9)

bipartiteGraph = Graph()




# print(graph.getNodeByID(n1.nodeId).neighbors)
print(n1.neighbors)
print('id  cost')
for node in graph.nodes.values():
    for key, value in graph.getNodeByID(node.nodeId).neighbors.items(): #for key, value in node.neighbors.items():
        print(str(node.nodeId) + ' -> ' + str(key) + ' = ' + str(value.distance))

# ret = aStarSearch(graph, graph.getNodeByID(n1.nodeId), graph.getNodeByID(n4.nodeId))
ret = pizzaDelivery(graph, graph.nodes[n0.nodeId], [graph.edges[2], graph.edges[3]])
for node_list in ret:
    print("Path part: ")
    for node in node_list:
        print(node.nodeId)

for a in ret:
    print
    # assert(path == 0->3->4)