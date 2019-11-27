from AStar import *
from Graph import *

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

print(graph.getNode(n1.nodeId).neighbors)
print('id  cost')
for node in graph.nodes.values():
    for key, value in graph.getNode(node.nodeId).neighbors.items():
        print(str(node.nodeId) + ' -> ' + str(key) + ' = ' + str(value.distance))

ret = aStarSearch(graph, graph.getNode(n1.nodeId), graph.getNode(n4.nodeId))

for a in ret:
    print
    # assert(path == 0->3->4)