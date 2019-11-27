from Graph import Graph
from AStar import a_star
def boolFromChar(c):
    return not 'f' == c

file = open('graf0.txt', 'r')
v1 = 0
v2 = 0
cost = 0
pizza = False
num_nodes = file.readline()

num_nodes = int(file.readline())
graph = Graph(num_nodes)
print('n: '+ str(num_nodes))

for line in file:
    if line == 'eof':
        break
    dict = line.split(' ')
    v1 = dict[0]
    v2 = dict[1]
    cost = dict[2]
    pizza = boolFromChar(dict[3])

start = 0
end  = num_nodes - 1

a_star(graph, start, end)
file.close()


