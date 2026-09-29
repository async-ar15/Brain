# Theory - Advanced Graphs (Dijkstra, MST, Union-Find)

These algorithms are usually reserved for Hard problems or very specific Medium problems.

## 1. Dijkstra's Algorithm (Shortest Path in Weighted Graphs)

**Goal:** Find the absolute shortest path from a `start` node to a `target` node in a graph where edges have positive weights.

**How it works:**
It's exactly like Graph BFS, but instead of a standard `Queue`, we use a `PriorityQueue` (Min-Heap) sorted by the *total cost* to reach a node.
By always popping the node with the lowest total cost, the *first time* we pop the target node, we are mathematically guaranteed that it is the absolute cheapest path to get there!

**Template snippet:**
```java
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
// pq stores: [node, total_cost_from_start]
pq.offer(new int[]{startNode, 0});

// Use a visited set to avoid expanding the same node twice
Set<Integer> visited = new HashSet<>();

while (!pq.isEmpty()) {
    int[] curr = pq.poll();
    int node = curr[0], cost = curr[1];
    
    if (node == target) return cost;
    if (visited.contains(node)) continue; // Already found a cheaper way here
    visited.add(node);
    
    for (int[] edge : adjList.get(node)) {
        int nextNode = edge[0], edgeWeight = edge[1];
        if (!visited.contains(nextNode)) {
            pq.offer(new int[]{nextNode, cost + edgeWeight});
        }
    }
}
```

## 2. Minimum Spanning Tree (MST)

**Goal:** Connect ALL nodes in a graph with the absolute minimum total edge weight. (e.g. Laying fiber optic cables to connect 5 cities as cheaply as possible).

### Prim's Algorithm
Start at any node. Add all its edges to a Min-Heap. Pop the smallest edge. If it leads to an unvisited node, add it to your MST, mark visited, and add its edges to the Min-Heap. Repeat until all nodes are visited. (Very similar code to Dijkstra, but the heap stores `[node, edge_weight]` instead of total cost).

## 3. Disjoint Set / Union-Find

**Goal:** An ultra-fast data structure to track which components are connected, and to instantly check if an edge forms a cycle. (Kruskal's Algorithm for MST uses this).

**How it works:**
Every node starts as its own "parent" (its own set). When we add an edge between A and B, we find the "absolute root parent" of A, and the "absolute root parent" of B. If they are different, we merge the sets by making A's root point to B's root. If they are the SAME, it means A and B were already connected by some other path, so this new edge forms a cycle!

```java
class UnionFind {
    int[] parent;
    
    public UnionFind(int n) {
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i; // Everyone is their own root initially
    }
    
    // Find absolute root with Path Compression (makes future lookups O(1))
    public int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]); 
    }
    
    // Union two sets. Returns false if they were already connected (cycle!)
    public boolean union(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI == rootJ) return false;
        parent[rootI] = rootJ;
        return true;
    }
}
```
