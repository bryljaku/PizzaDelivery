#include <iostream>
#include <fstream>

int main(int argc, char* argv[]) {
        std::fstream graphFile;
        
        int vertice1, vertice2;
        int sizeOfGivenGraph;
        if (argc < 2){
            std::cout<<"No arguments given\n";
            return 1;
        }
        
        for (int i = 1; i < argc; i++) {
            if (argc != 2)
                std::cout<<"test"<<i<<'\n';
            std::string fileName = argv[i];
            graphFile.open(fileName);
            if (!graphFile.good()) {
                std::cout << "File not found\n";
                return 3;
            }
            
            graphFile >> sizeOfGivenGraph;
            if (sizeOfGivenGraph < 4)
                break;
            while (!graphFile.eof()) {
                graphFile >> vertice1 >> vertice2;
            }
            
            graphFile.close();
            return 0;
}
}