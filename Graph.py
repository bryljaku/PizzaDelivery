
class Graph:
    data = 0
    def __init__(self, num):
        self.data = num

    def add_edge(self, edge):
        print("This is a message inside the class." + str(self.data))

