class Vertex:
    def __init__(self, id, cost):
        self.id = id
        self.cost = cost
        self.adjacent = []
        self.path = []


# class Edge:
#     def __init__(self, v1, v2, weight, to_visit = False):
#         self.v1 = v1
#         self.v2 = v2
#         self.edge_pair = (min(v1, v2), max(v1, v2))
#         self.weight = weight
#         self.to_visit = to_visit


class Graph:
    def __init__(self, size):
        self.size = size
        # self.vertices = []
        # self.edges = []
        self.graph_representation = {}  # dictionary which keys are vertices and values are tuples of adjacent vertices,
                                        # weights of edge and if edge must be visited
    # def add_vertex(self, vertex):

    def get_cost(self, v1, v2):
        if v1 or v2 not in self.graph_representation:
            return None

        # TODO



    # def add_edge(self, edge):
    #     self.edges.append(edge)

