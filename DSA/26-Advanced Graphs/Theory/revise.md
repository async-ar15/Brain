# Advanced Graphs — Revision Sheet

---

## 01. Network Delay Time

**In My Words:** You are given a network of `n` nodes, labeled from 1 to `n`. You are given `times`, a list of travel times as directed edges `times[i] = (u, v, w)`. We send a signal from a given node `k`. Return the minimum time it takes for all `n` nodes to receive the signal. If it is impossible for all `n` nodes to receive the signal, return -1.

**Constraint Whispers:**
- Finding the time it takes for ALL nodes to receive a signal is equivalent to finding the absolute *longest* of all the *shortest paths* from `k` to every node.
- "Shortest path in weighted graph" screams Dijkstra's Algorithm.

**The Bridge:** Run Dijkstra's starting at node `k`. We maintain a `visited` set to ensure we only process the absolute shortest path to each node. When we process a node, it receives the signal at that exact `time`. The maximum `time` we ever process is the final answer, *provided* we eventually visited all `n` nodes.

**Optimized Intuition:**
1. Build Adjacency List: `Map<Integer, List<int[]>>`. `int[]` is `[neighbor, weight]`.
2. Priority Queue: `new PriorityQueue<>((a, b) -> a[1] - b[1])`. Array is `[node, total_time]`. Add `[k, 0]`.
3. `visited` Set. `maxTime = 0`.
4. While PQ is not empty: `poll()` current node.
5. If `visited.contains(node)`, continue. Else, `visited.add(node)`.
6. `maxTime = Math.max(maxTime, time)`.
7. Loop through neighbors. If not visited, `offer` to PQ `[neighbor, time + weight]`.
8. Return `visited.size() == n ? maxTime : -1`.

**Template:** Dijkstra's Algorithm

**Time:** $O(E \log V)$ | **Space:** $O(V + E)$

**Code Solution:**
```java
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<int[]>> adj = new HashMap<>();
        for (int i = 1; i <= n; i++) adj.put(i, new ArrayList<>());
        
        for (int[] time : times) {
            adj.get(time[0]).add(new int[]{time[1], time[2]});
        }
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.offer(new int[]{k, 0});
        
        Set<Integer> visited = new HashSet<>();
        int maxTime = 0;
        
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int node = curr[0], time = curr[1];
            
            if (visited.contains(node)) continue;
            visited.add(node);
            
            maxTime = Math.max(maxTime, time);
            
            for (int[] edge : adj.get(node)) {
                int nextNode = edge[0], weight = edge[1];
                if (!visited.contains(nextNode)) {
                    pq.offer(new int[]{nextNode, time + weight});
                }
            }
        }
        
        return visited.size() == n ? maxTime : -1;
    }
}
```

---

## 02. Min Cost to Connect All Points

**In My Words:** You are given an array `points` representing X-Y coordinates. The cost of connecting two points is the Manhattan distance: $|xi - xj| + |yi - yj|$. Return the minimum cost to make all points connected.

**The Bridge:** "Minimum cost to make all points connected" is the EXACT literal definition of a Minimum Spanning Tree (MST). You can solve this with either Prim's Algorithm (Priority Queue) or Kruskal's Algorithm (Union-Find). Prim's is often easier to write for dense graphs (like this one, where every point can connect to every other point).

**Optimized Intuition (Prim's):**
1. Adjacency list isn't needed upfront since cost is easily calculated on the fly.
2. PQ sorted by distance. Array is `[point_index, distance_from_tree]`. Start with `[0, 0]`.
3. `visited` set. `totalCost = 0`.
4. While `visited.size() < points.length`:
   - `poll()` the closest point. If visited, continue.
   - `visited.add(index)`. `totalCost += dist`.
   - Loop through ALL other points. If `!visited`, calculate Manhattan distance, and `offer` to PQ.
5. Return `totalCost`.

**Time:** $O(N^2 \log N)$ | **Space:** $O(N^2)$ (PQ can get large)

**Code Solution:**
```java
class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.offer(new int[]{0, 0});
        
        Set<Integer> visited = new HashSet<>();
        int totalCost = 0;
        
        while (visited.size() < n) {
            int[] curr = pq.poll();
            int i = curr[0], cost = curr[1];
            
            if (visited.contains(i)) continue;
            visited.add(i);
            totalCost += cost;
            
            for (int j = 0; j < n; j++) {
                if (!visited.contains(j)) {
                    int dist = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                    pq.offer(new int[]{j, dist});
                }
            }
        }
        
        return totalCost;
    }
}
```

---

## 03. Redundant Connection

**In My Words:** In a tree (which is a connected acyclic graph), one extra edge was added, creating a cycle. Find and return that redundant edge. (If there are multiple, return the one that appears last in the input).

**The Bridge:** We are adding edges one by one and we need to detect the EXACT moment a cycle is formed. This is the ultimate use case for Union-Find (Disjoint Set). 
If we try to union two nodes, and they ALREADY have the same root parent, then the edge we are trying to add forms a cycle! That edge is the redundant one.

**Optimized Intuition:**
1. Build a `UnionFind` class with `find(int x)` and `union(int x, int y)`.
2. Initialize `UnionFind(n + 1)`.
3. Iterate through the given `edges`.
4. If `!uf.union(edge[0], edge[1])` (meaning they were already connected), return `edge`.

**Template:** Union-Find

**Time:** $O(N \cdot \alpha(N))$ roughly $O(N)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    class UnionFind {
        int[] parent;
        
        public UnionFind(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        
        public int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]); // Path compression
        }
        
        public boolean union(int i, int j) {
            int rootI = find(i);
            int rootJ = find(j);
            
            if (rootI == rootJ) return false; // Cycle detected!
            
            parent[rootI] = rootJ;
            return true;
        }
    }
    
    public int[] findRedundantConnection(int[][] edges) {
        UnionFind uf = new UnionFind(edges.length + 1); // 1-indexed
        
        for (int[] edge : edges) {
            if (!uf.union(edge[0], edge[1])) {
                return edge; // This is the edge that caused the cycle
            }
        }
        
        return new int[0];
    }
}
```
