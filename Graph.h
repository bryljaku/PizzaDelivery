#include <iostream>
#include <queue>

#ifndef GRAFY_GRAPH_H
#define GRAFY_GRAPH_H

class Edge {
public:
    int vertice1, vertice2;
    int cost;
    bool toVisit;
    Edge(int v1, int v2, int c, bool toVis = false): vertice1(v1), vertice2(v2), cost(c), toVisit(toVis) {};
};

class Graph
{
private:
    std::vector<std::vector<int>> neighboursOfEdges;
    std::vector<Edge> allEdges;

public:
    Graph(int givenSize) : neighboursOfEdges(std::vector<std::vector<int>>(givenSize))
    {}

    void addEdge(int vertice1, int vertice2, int cost, bool toVisit)
    {
        if (vertice1 == vertice2)
            return;
        Edge newEdge = new Edge(vertice1, vertice2, cost, toVisit);

        for (auto edge : allEdges)
            if (edge == newEdge)
                return;

        allEdges.emplace_back(newEdge);
        neighboursOfEdges[vertice1].emplace_back(vertice2);
        neighboursOfEdges[vertice2].emplace_back(vertice1);
    }
    void printEdges()
    {
        for (auto edge : allEdges)
            std::cout<<edge.first<<' '<< edge.second<<'\n';
        std::cout<<"\n";
    }

};
#endif //GRAFY_GRAPH_H
