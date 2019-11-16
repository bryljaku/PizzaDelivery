
file = open('graf0.txt', 'r')
v1 = 0
v2 = 0
cost = 0
pizza = False
num_nodes = file.readline()

print('n: '+ str(num_nodes))
for line in file:
    print(line)
    dict = line.split(' ')
    v1 = dict[0]
    v2 = dict[1]
    cost = dict[2]
    pizza = dict[3]

file.close()

