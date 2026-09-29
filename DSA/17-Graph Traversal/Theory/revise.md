# Graphs — Revision Sheet

---

## 01. Number of Islands

**In My Words:** Given an $m \times n$ 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

**The Bridge:** This is the classic "Connected Components" problem on an implicit graph (matrix). Every time we find a piece of land ('1') that we haven't visited yet, it must be part of a NEW island! We increment our count, and then we run DFS to "sink" (mark as visited) the entire island so we don't count its parts again.

**Optimized Intuition:** 
Nested `for` loops through every cell in the grid.
If `grid[r][c] == '1'`:
  `islands++`
  `dfs(grid, r, c)`
The DFS: If out of bounds or `== '0'`, return. Mark `grid[r][c] = '0'` (sinking it acts as our `visited` set). Call DFS on 4 neighbors.

**Time:** $O(M \cdot N)$ | **Space:** $O(M \cdot N)$ (Worst case call stack if whole grid is land)

**Code Solution:**
```java
class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        
        int islands = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == '1') {
                    islands++;
                    dfs(grid, r, c);
                }
            }
        }
        return islands;
    }
    
    private void dfs(char[][] grid, int r, int c) {
        if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == '0') {
            return;
        }
        
        grid[r][c] = '0'; // Mark visited by sinking it
        
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
}
```

---

## 02. Max Area of Island

**In My Words:** Return the maximum area (number of '1's) of an island in a given 2D grid.

**The Bridge:** Exactly the same logic as Number of Islands. But instead of just sinking the island, we need our DFS to return the *size* of the island it just explored.

**Optimized Intuition:** 
Nested loops. `maxArea = max(maxArea, dfs(grid, r, c))`.
The DFS: If out of bounds or '0', return `0`.
Mark visited `grid[r][c] = '0'`.
Return `1 + dfs(up) + dfs(down) + dfs(left) + dfs(right)`.

**Time:** $O(M \cdot N)$ | **Space:** $O(M \cdot N)$

**Code Solution:**
```java
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == 1) {
                    maxArea = Math.max(maxArea, dfs(grid, r, c));
                }
            }
        }
        return maxArea;
    }
    
    private int dfs(int[][] grid, int r, int c) {
        if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == 0) {
            return 0;
        }
        
        grid[r][c] = 0; // Sink it
        
        return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + 
                   dfs(grid, r, c + 1) + dfs(grid, r, c - 1);
    }
}
```

---

## 03. Clone Graph

**In My Words:** Return a deep copy (clone) of a graph.

**The Bridge:** As we traverse the graph, we must create copies of the nodes. But if node A points to node B, and node B points to node A, we might create an infinite loop of cloning! We need a way to remember: "Have I already cloned this node?"

**Optimized Intuition:** 
Use a `HashMap<Node, Node> clonedMap` where Key = Original Node, Value = Cloned Node.
DFS function: If original node is in map, return the cloned value.
Else, create a new cloned node (just value, empty neighbors). Add to map immediately!
Iterate through original node's neighbors. For each neighbor, recursively call DFS and add the returned node to the cloned node's neighbor list.
Return the cloned node.

**Time:** $O(V + E)$ | **Space:** $O(V)$

**Code Solution:**
```java
class Solution {
    private Map<Node, Node> map = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) return null;
        
        // If we already cloned this node, return the clone to prevent cycles
        if (map.containsKey(node)) {
            return map.get(node);
        }
        
        // Create the clone (without neighbors yet)
        Node clone = new Node(node.val, new ArrayList<>());
        // Put in map IMMEDIATELY before exploring neighbors
        map.put(node, clone);
        
        // Clone all neighbors
        for (Node neighbor : node.neighbors) {
            clone.neighbors.add(cloneGraph(neighbor));
        }
        
        return clone;
    }
}
```

---

## 04. Pacific Atlantic Water Flow

**In My Words:** Given a grid of heights, find all coordinates where water can flow to BOTH the Pacific (top/left) and Atlantic (bottom/right) oceans. Water flows from higher/equal height to lower/equal height.

**Constraint Whispers:**
- Trying to run a DFS *from* every cell to see if it reaches the oceans will lead to a lot of repeated work and TLE.

**The Bridge:** Think in reverse! Instead of water flowing down to the ocean, what if the ocean water flowed UP onto the island? We can start a DFS from all the coastal cells, moving only to cells with GREATER OR EQUAL height. Any cell the Pacific can reach gets marked in a `pacific` boolean matrix. Any cell the Atlantic can reach gets marked in an `atlantic` boolean matrix. The answer is the cells marked true in BOTH matrices.

**Optimized Intuition:**
Create `pacificVisited` and `atlanticVisited` boolean matrices.
Loop along the left/right borders and start DFS for Pacific/Atlantic.
Loop along top/bottom borders and start DFS.
The DFS condition to continue: next cell height $\ge$ current cell height.
After all DFS, loop through the whole grid. If `pacificVisited[r][c] && atlanticVisited[r][c]`, add to result.

**Time:** $O(M \cdot N)$ | **Space:** $O(M \cdot N)$

**Code Solution:**
```java
class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        int rows = heights.length;
        int cols = heights[0].length;
        
        boolean[][] pac = new boolean[rows][cols];
        boolean[][] atl = new boolean[rows][cols];
        
        // Run DFS from coastal borders
        for (int c = 0; c < cols; c++) {
            dfs(heights, 0, c, pac, heights[0][c]);       // Top
            dfs(heights, rows - 1, c, atl, heights[rows - 1][c]); // Bottom
        }
        
        for (int r = 0; r < rows; r++) {
            dfs(heights, r, 0, pac, heights[r][0]);       // Left
            dfs(heights, r, cols - 1, atl, heights[r][cols - 1]); // Right
        }
        
        // Find cells that can reach both
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (pac[r][c] && atl[r][c]) {
                    res.add(Arrays.asList(r, c));
                }
            }
        }
        
        return res;
    }
    
    private void dfs(int[][] heights, int r, int c, boolean[][] visited, int prevHeight) {
        if (r < 0 || c < 0 || r >= heights.length || c >= heights[0].length 
            || visited[r][c] || heights[r][c] < prevHeight) {
            return;
        }
        
        visited[r][c] = true;
        
        dfs(heights, r + 1, c, visited, heights[r][c]);
        dfs(heights, r - 1, c, visited, heights[r][c]);
        dfs(heights, r, c + 1, visited, heights[r][c]);
        dfs(heights, r, c - 1, visited, heights[r][c]);
    }
}
```
