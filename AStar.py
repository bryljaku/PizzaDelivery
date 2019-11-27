import typing
from PriorityQueue import HeapPriorityQueue as PriorityQueue
from Graph import *

def calculateHeuristic(nodeA: Node, nodeB: Node) -> float:
    distX = (nodeA.x - nodeB.x)
    distY = (nodeA.y - nodeB.y)
    return math.sqrt((distX * distX) + (distY * distY))


def reconstructPath(cameFrom, goal):
    path = [goal]
    curr = goal
    while cameFrom[curr] is not None:
        curr = cameFrom[curr]
        path.append(curr)
    path.reverse()
    return path

def aStarSearch(graph: Graph, start: Node, goal: Node):
    toVisit:PriorityQueue[Node] = PriorityQueue()
    toVisit.put(start, 0)
    cameFrom = {}
    currentCost = {}
    cameFrom[start] = None
    currentCost[start] = 0

    while not toVisit.empty():
        current = toVisit.get()
        print(current.nodeId)
        if current == goal:
            break

        for node in graph.getNode(current.nodeId).neighbors.values():
            next = graph.getNode(node.nodeId)
            newCost = currentCost[current] + graph.cost(current, next)
            if next not in currentCost or newCost < currentCost[next]:
                currentCost[next] = newCost
                priority = newCost + calculateHeuristic(goal, next)
                toVisit.put(next, priority)
                cameFrom[next] = current

    return reconstructPath(cameFrom, goal), currentCost


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