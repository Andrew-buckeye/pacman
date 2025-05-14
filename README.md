Making Pacman easier cuz I suck at it

Implementation: The PACMAN game map, whether it's AI or manually played, is based on a tile system.
A 50 by 50 grid is used to hold pellets, characters, and walls. Having this in place allows us to treat 
the game like a graph, and computer scientists love graphs.

Algoithms used

Breadth First Search- BFS is a graph traversal algorithm beginning with the first node, and then going to all the adjacent nodes, then those adjacent nodes, until all nodes have been visited. More on [BFS](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)

Depth First Search- Stuck and tired of coding this 5/14/25
DFS algo gets first pellet and then bounces off the wall, staying like that. Think I may need to restructure
AI_driver for this
    
                              