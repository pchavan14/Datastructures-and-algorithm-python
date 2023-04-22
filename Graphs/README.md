- Graphs consist of nodes and edges which connects these nodes
- DS used to identify the shortest path
- graph DS can handle cyclic connections

## **Graph terminologies** 
- Vertices are the node of the graph
- Edge is the line that connect pair of vertices
- Unweighted and weighted which has weight to the edge
- Undirected graph - In case the edges of the graph do not have a direction associated with them
- Directed graph - In case the edges have direction and tells us how we can travel from one edge to another
- Cyclic graph - A graph which has atleast one loop
- Acyclic graph - A graph with no loop
- Tree - is a DAG

## **BFS vs DFS** 
- BFS like level order traversal
- DFS goes as deep as possible and then do backtracking
- BFS uses queue
- DFS uses stack
- BFS are used to search when we know target is near to vertex
- DFS are used to search when we know target is far from the vertex


## **Single source shortest path**
- BFS can be used for SSSP algorithm only with unweighted, undirected graphs and unweighted , directed graphs
- DFS does not work for SSSP

