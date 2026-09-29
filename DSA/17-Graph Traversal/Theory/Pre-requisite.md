# 18. Graphs - Pre-requisites

## What is a Graph?

A Graph is a collection of **Nodes** (vertices) connected by **Edges**. 
A Tree is actually just a specific type of Graph (one that is connected and has no cycles).

Graphs can represent almost any network: social networks (friends), road maps (cities and highways), internet routing, or course prerequisites.

## Types of Graphs
1. **Directed vs Undirected:** Edges can be one-way streets (Directed) or two-way streets (Undirected).
2. **Weighted vs Unweighted:** Edges can have a "cost" or "distance" associated with them.
3. **Cyclic vs Acyclic:** A graph with at least one loop is Cyclic. A Directed Acyclic Graph is called a **DAG**.

## How are Graphs Represented in Code?

LeetCode rarely gives you actual `Node` objects for graphs (unlike Trees). Usually, they give you an array of edges, e.g., `edges = [[0, 1], [1, 2], [2, 0]]` meaning node 0 connects to 1, 1 to 2, 2 to 0.

You must build the graph representation yourself before running algorithms.

### 1. Adjacency Matrix
A 2D boolean (or int) array `matrix[i][j]` that is true if there's an edge between node `i` and `j`. 
- **Pros:** $O(1)$ to check if an edge exists.
- **Cons:** $O(V^2)$ space (wasteful for sparse graphs), $O(V)$ to find all neighbors of a node.

### 2. Adjacency List (Use this 99% of the time)
A HashMap or Array of Lists where `map.get(i)` returns a list of all neighbors of node `i`.
- **Pros:** Efficient space $O(V + E)$, extremely fast to iterate over a node's neighbors.

```java
// Building an Adjacency List from an Edges array (Undirected Graph)
int n = 5; // Number of nodes
List<List<Integer>> adjList = new ArrayList<>();
for (int i = 0; i < n; i++) {
    adjList.add(new ArrayList<>());
}

int[][] edges = {{0, 1}, {1, 2}, {2, 0}};
for (int[] edge : edges) {
    int u = edge[0];
    int v = edge[1];
    
    // Add connection in both directions (since undirected)
    adjList.get(u).add(v);
    adjList.get(v).add(u);
}
```

## The Visited Set
Unlike Trees, Graphs can have cycles. If you run DFS on a graph with a cycle without tracking where you've been, you will infinite loop and get a StackOverflow error.
**You MUST maintain a `visited` HashSet (or boolean array) in almost every graph algorithm.**
