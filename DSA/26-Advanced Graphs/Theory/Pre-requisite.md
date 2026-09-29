# 21. Advanced Graphs - Pre-requisites

## Going Beyond DFS and BFS

DFS and BFS are powerful, but they have limitations:
- **BFS** can only find the shortest path in an **Unweighted Graph**. If edges have different costs (e.g., Highway A costs $5, Highway B costs $10), BFS fails.
- **DFS/BFS** cannot efficiently find Minimum Spanning Trees (the cheapest way to connect all nodes so there are no islands).

For these scenarios, we need specialized algorithms created by computer science pioneers.

## Weighted Graphs

In Advanced Graphs, edges have weights.
Instead of an Adjacency List looking like `Map<Integer, List<Integer>>` (just neighbors), it looks like `Map<Integer, List<int[]>>`, where the array is `[neighbor, weight]`.

## Priority Queues (Min-Heaps)

Almost all advanced graph algorithms (Dijkstra, Prim, Kruskal) rely heavily on a **Min-Heap** (Priority Queue in Java). 
The core philosophy is greedy: "At this exact moment, what is the CHEAPEST edge I can take?" A Min-Heap answers this question instantly.
