# Theory - Union Find

Union-Find is a magical template. If you memorize the class structure below, you can solve Hard graph connectivity problems trivially.

## Where is it commonly used?
1. **Cycle Detection in Undirected Graphs:** The moment you try to `Union(A, B)` and they already have the same root, you've found a cycle! (e.g. Redundant Connection).
2. **Kruskal's Algorithm:** Finding the Minimum Spanning Tree.
3. **Dynamic Connectivity:** Connecting provinces, islands, or checking if paths exist.

## The Two Optimizations

A naive Union-Find can devolve into a linked list, making `Find()` take $O(N)$ time. We must use two optimizations to keep it $O(1)$:

1. **Path Compression (Crucial):** Whenever you call `Find(i)`, don't just return the root. *Reassign* `parent[i]` to point directly to the root. This flattens the tree completely.
2. **Union by Rank (Optional but good):** When merging two trees, always attach the shorter tree to the root of the taller tree. This keeps the tree shallow.

### Template: Optimized Union-Find Class

```java
class UnionFind {
    private int[] parent;
    private int[] rank; // Used to keep tree flat
    public int count;   // Number of disjoint components

    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        count = n;
        
        // Initially, everyone is their own parent (root)
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
    }
    
    // Find with Path Compression
    public int find(int i) {
        if (parent[i] == i) {
            return i;
        }
        // Recursively find root, and reassign current node's parent DIRECTLY to the root
        return parent[i] = find(parent[i]); 
    }
    
    // Union by Rank. Returns false if they were already connected.
    public boolean union(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        
        if (rootI == rootJ) {
            return false; // Cycle detected!
        }
        
        // Attach smaller tree under larger tree
        if (rank[rootI] > rank[rootJ]) {
            parent[rootJ] = rootI;
        } else if (rank[rootI] < rank[rootJ]) {
            parent[rootI] = rootJ;
        } else {
            // Same rank, pick one arbitrarily and increase its rank
            parent[rootJ] = rootI;
            rank[rootI]++;
        }
        
        count--; // We merged two components into one
        return true;
    }
}
```

# Your interview cheat code

```text
1. Are you merging groups together or adding edges dynamically?
                  ↓
2. Do you need to detect cycles in an undirected graph?
                  ↓
           PASTE THE UNION-FIND CLASS TEMPLATE
```
