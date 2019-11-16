
class Graph:
    data = 0
    def __init__(self, num):
        self.data = num

    def function(self):
        print("This is a message inside the class." + str(self.data))

myobjectx = Graph(10)
myobjectx.function()
