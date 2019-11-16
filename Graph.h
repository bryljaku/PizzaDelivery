#include <iostream>
#include <queue>

#ifndef GRAFY_GRAPH_H
#define GRAFY_GRAPH_H
class Graph
{
private:
    std::vector<std::vector<int>> neighboursOfEdges;
    std::vector<std::pair<int, int>> allEdges;

public:
    Graph(int givenSize) : neighboursOfEdges(std::vector<std::vector<int>>(givenSize))
    {}

    void addEdge(int vertice1, int vertice2)
    {
        if (vertice1 == vertice2)
            return;
        std::pair<int, int> newEdge = std::make_pair(std::min(vertice1, vertice2), std::max(vertice1, vertice2));

        for (auto edge : allEdges)
            if (edge == newEdge)
                return;

        allEdges.emplace_back(newEdge);
        neighboursOfEdges[vertice1].emplace_back(vertice2);
        neighboursOfEdges[vertice2].emplace_back(vertice1);
    }

    void checkIfBridge(int vertice1, int vertice2)
    {
        int currentVertice = 0;

        std::vector<bool> visitedVertices(neighboursOfEdges.size(), false);
        std::queue<int> queueOfVertices;

        while (currentVertice == vertice1 || currentVertice == vertice2)
            currentVertice++;


        visitedVertices[currentVertice] = true;
        visitedVertices[vertice1] = true;
        visitedVertices[vertice2] = true;
        queueOfVertices.push(currentVertice);

        do {
            currentVertice = queueOfVertices.front();
            queueOfVertices.pop();
            for (auto i : neighboursOfEdges[currentVertice])
                if (!visitedVertices[i]){
                    queueOfVertices.push(i);
                    visitedVertices[i] = true;
                }
        } while (!queueOfVertices.empty());

        for (auto i : visitedVertices)
            if (!i) {
                std::cout << vertice1 << ' ' << vertice2 << '\n';
                return;
            }
    }
    void printBridges()
    {
        if (neighboursOfEdges.size() > 2)
            for (auto edge : allEdges)
                checkIfBridge(edge.first, edge.second);
    }
    void printEdges()
    {
        for (auto edge : allEdges)
            std::cout<<edge.first<<' '<< edge.second<<'\n';
        std::cout<<"\n";
    }

};
#endif //GRAFY_GRAPH_H
