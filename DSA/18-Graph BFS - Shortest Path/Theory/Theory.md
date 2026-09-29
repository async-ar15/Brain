# Theory - Graph BFS (Shortest Path)

Graph BFS is the definitive algorithm for finding the shortest path in an unweighted graph or matrix.

## Where is it commonly used?
1. **Shortest Path (Unweighted):** Shortest path out of a maze, minimum steps to transform a word (Word Ladder).
2. **Multi-Source BFS:** Fire spreading, water rotting oranges.

## Strong signals to look for
- "Find the **shortest path**"
- "Find the **minimum number of steps/moves**"
- The graph/grid has unweighted edges (all moves cost 1).

## The Multi-Source BFS Pattern (Rotting Oranges)

Sometimes, instead of finding the shortest path from a single start node to an end node, a problem asks how long it takes for a condition to spread across a grid (like a fire spreading from multiple source points).

**The Trick:** Instead of initializing the Queue with just one starting node, you loop through the entire grid and add ALL the source nodes to the Queue at the very beginning (Queue size > 1 before the loop starts). Then run normal BFS. They will all radiate outwards simultaneously, layer by layer!

### Template: Graph BFS (Shortest Path / Levels)

```java
public int shortestPathBFS(int[][] grid, int startR, int startC) {
    Queue<int[]> queue = new LinkedList<>();
    boolean[][] visited = new boolean[grid.length][grid[0].length];
    
    // 1. Initialize queue with start node(s) and mark visited immediately
    queue.offer(new int[]{startR, startC});
    visited[startR][startC] = true;
    
    int steps = 0; // Tracks the radius of our search
    int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    
    // 2. Loop while queue is not empty
    while (!queue.isEmpty()) {
        int size = queue.size();
        
        // 3. Process the current level
        for (int i = 0; i < size; i++) {
            int[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];
            
            // Check if we reached the goal
            if (grid[r][c] == TARGET) return steps;
            
            // Explore neighbors
            for (int[] dir : directions) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                
                // Bounds and visited check
                if (nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length && !visited[nr][nc]) {
                    queue.offer(new int[]{nr, nc});
                    visited[nr][nc] = true; // MARK VISITED IMMEDIATELY!
                }
            }
        }
        
        steps++; // Finished exploring this distance, increment step counter
    }
    
    return -1; // Target not reachable
}
```

# Your interview cheat code

```text
1. Does it ask for the Shortest Path or Min Steps? (And edges are unweighted)
                  ↓
2. Are there multiple starting points? (Add all to queue first!)
                  ↓
           USE GRAPH BFS (Queue + Visited Set)
```
