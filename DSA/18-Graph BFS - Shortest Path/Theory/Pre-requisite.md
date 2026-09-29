# 19. Graph BFS (Shortest Path) - Pre-requisites

## DFS vs BFS on Graphs

In Trees, we used DFS for going deep and BFS for level-by-level traversal. In Graphs, the distinction becomes much more important because of **Pathfinding**.

- **DFS** will find *a* path between two nodes, but it is rarely the *shortest* path. It dives down random wormholes until it hits a dead end.
- **BFS** explores equally in all directions, radiating outward like a ripple in a pond. Because of this ripple effect, the very first time BFS reaches a target node, it is **mathematically guaranteed to be the Shortest Path** (assuming unweighted edges).

## The Queue and Visited Set

Just like Tree BFS, Graph BFS relies heavily on a `Queue`.
However, because graphs have cycles, we also absolutely require a `visited` set.

**CRITICAL RULE FOR GRAPH BFS:**
You MUST mark a node as `visited` the exact moment you *add it to the Queue*, **NOT** when you *remove it from the Queue*.

If you wait until you pop it from the Queue to mark it visited, multiple other nodes might see it as "unvisited" and add it to the Queue again, causing exponential blowup and TLE/MLE.

```java
// CORRECT WAY
queue.offer(neighbor);
visited.add(neighbor); // Mark visited IMMEDIATELY upon enqueueing
```
