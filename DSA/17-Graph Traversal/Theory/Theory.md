# Theory - Graphs (DFS / Connected Components)

Graph problems can look intimidating, but they almost all break down into building an Adjacency List and then running a standard DFS or BFS.

## Where is it commonly used?
1. **Connected Components:** Finding groups of islands, clusters of friends.
2. **Pathfinding:** Can I get from point A to point B?
3. **Cycle Detection:** Does this graph have a loop?

## Strong signals to look for
- "Number of provinces/islands"
- "Are these nodes connected?"
- You are given a list of `edges` or connections.

## Graph DFS Template

Once you build the adjacency list, DFS is identical to Tree DFS, with the crucial addition of the `visited` set.

```java
public void graphDFS(int n, int[][] edges) {
    // 1. Build Adjacency List
    List<List<Integer>> adjList = new ArrayList<>();
    for(int i = 0; i < n; i++) adjList.add(new ArrayList<>());
    for (int[] edge : edges) {
        adjList.get(edge[0]).add(edge[1]);
        adjList.get(edge[1]).add(edge[0]); // Undirected
    }
    
    // 2. Visited Array
    boolean[] visited = new boolean[n];
    
    // 3. For disconnected graphs, we must loop through all nodes
    // to ensure we don't miss components that aren't connected to node 0.
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            // This triggers a full DFS for one connected component
            dfs(i, adjList, visited);
        }
    }
}

private void dfs(int node, List<List<Integer>> adjList, boolean[] visited) {
    // Mark current node as visited immediately
    visited[node] = true;
    
    // Process node here if needed
    
    // Visit all neighbors
    for (int neighbor : adjList.get(node)) {
        if (!visited[neighbor]) {
            dfs(neighbor, adjList, visited);
        }
    }
}
```

## Implicit Graphs (Matrix as a Graph)

Sometimes the graph isn't given as nodes and edges. It's given as a 2D grid (like a maze or a map of islands).
In this case, you don't need to build an Adjacency List! The grid itself IS the graph.
- A cell `(r, c)` is a node.
- The edges are implicitly the 4 cardinal directions: `(r+1, c)`, `(r-1, c)`, `(r, c+1)`, `(r, c-1)`.

```java
// DFS on a Matrix
private void dfsMatrix(int[][] grid, int r, int c) {
    // Bounds check and visited check
    if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == 0) {
        return; 
    }
    
    // Mark visited (by mutating the grid if allowed, e.g. turning land 1 into water 0)
    grid[r][c] = 0; 
    
    // Explore neighbors
    dfsMatrix(grid, r + 1, c);
    dfsMatrix(grid, r - 1, c);
    dfsMatrix(grid, r, c + 1);
    dfsMatrix(grid, r, c - 1);
}
```

# Your interview cheat code

```text
1. Are you given nodes and edges?
                  ↓
2. BUILD AN ADJACENCY LIST FIRST.
                  ↓
3. Do you need to visit everything or find components?
                  ↓
           USE DFS + VISITED ARRAY
```
