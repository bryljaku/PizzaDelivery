from Graph import *
from AStar import *
from PizzaDelivery import *
import argparse

parser = argparse.ArgumentParser(description='PizzaDelivery path finder')
parser.add_argument("-input", action="store", required=True, type=str, help="file")

args = parser.parse_args()
fileName = args.input
file = open(fileName, 'r')

# get pizzeria
pizzeria = int(file.readline())
print(f'pizzeria = {pizzeria}')

graph = Graph()
#add nodes
for line in file:
    l = line.rstrip('\n')
    if '#' in l:
        break
    dict = l.split(' ')
    nodeId = int(dict[0])
    x = float(dict[1])
    y = float(dict[2])
    graph.addNode(Node(nodeId, x, y))

#add edges
pizzaEdges = []
for line in file:
    l = line.rstrip('\n')
    if 'eof' in l:
        break
    dict = l.split(' ')
    nodeId1 = int(dict[0])
    nodeId2 = int(dict[1])
    distance = float(dict[2])
    e = Edge(nodeId1, nodeId2, distance)
    if dict[3] == 'p':
        pizzaEdges.append(e)
    graph.addEdge(e)
file.close()


start = graph.getNodeByID(pizzeria)
pizzaDelivery(graph, start, pizzaEdges)
