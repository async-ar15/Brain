# Graph BFS — Revision Sheet

---

## 01. Rotting Oranges

**In My Words:** You are given an $m \times n$ grid where 0 is empty, 1 is a fresh orange, and 2 is a rotten orange. Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes until no cell has a fresh orange (or -1 if impossible).

**The Bridge:** This is the textbook example of Multi-Source BFS. The rot spreads from ALL initially rotten oranges simultaneously, radiating outwards layer by layer. The number of layers (minutes) it takes to finish spreading is our answer.

**Optimized Intuition:** 
1. Loop through grid. Count `freshOranges`. Enqueue all `[r, c]` where `grid[r][c] == 2` into our Queue.
2. If `freshOranges == 0`, return 0.
3. Run BFS. Maintain `minutes` counter. For every `size` loop, explore 4 directions.
4. If neighbor is bounds and `== 1` (fresh):
   - Make it rotten (`grid[nr][nc] = 2`). (This modifies grid IN-PLACE, acting as our visited set!)
   - `freshOranges--`
   - Enqueue neighbor.
5. After `size` loop completes, `minutes++`.
6. Return `freshOranges == 0 ? minutes - 1 : -1`. (Why -1? Because the final queue pop processing the last rotten oranges will increment `minutes` even though they have no fresh neighbors left to rot).

**Template:** Multi-Source BFS

**Time:** $O(M \cdot N)$ | **Space:** $O(M \cdot N)$

**Code Solution:**
```java
class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int freshCount = 0;
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) queue.offer(new int[]{r, c});
                else if (grid[r][c] == 1) freshCount++;
            }
        }
        
        if (freshCount == 0) return 0;
        
        int minutes = 0;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] curr = queue.poll();
                
                for (int[] d : dirs) {
                    int r = curr[0] + d[0];
                    int c = curr[1] + d[1];
                    
                    if (r >= 0 && c >= 0 && r < rows && c < cols && grid[r][c] == 1) {
                        grid[r][c] = 2;
                        freshCount--;
                        queue.offer(new int[]{r, c});
                    }
                }
            }
            minutes++;
        }
        
        return freshCount == 0 ? minutes - 1 : -1;
    }
}
```

---

## 02. Walls and Gates

**In My Words:** You are given an $m \times n$ grid representing rooms. -1 is a wall. 0 is a gate. INF is an empty room. Fill each empty room with the distance to its nearest gate. If impossible, leave as INF.

**The Bridge:** Exactly like Rotting Oranges! The gates are the sources. They radiate distance outwards simultaneously. This guarantees that whichever gate reaches an empty room first provides the absolute shortest distance.

**Optimized Intuition:**
1. Enqueue all gates `(value == 0)`.
2. Run BFS. For every neighbor that is an empty room (INF):
   - `grid[nr][nc] = grid[r][c] + 1`
   - Enqueue neighbor.
(Notice we don't need a separate `visited` set or a `steps` variable, because setting the room's value to anything other than INF inherently marks it as visited and records the distance simultaneously!).

**Template:** Multi-Source BFS

**Time:** $O(M \cdot N)$ | **Space:** $O(M \cdot N)$

**Code Solution:**
```java
class Solution {
    public void wallsAndGates(int[][] rooms) {
        if (rooms == null || rooms.length == 0) return;
        
        int rows = rooms.length;
        int cols = rooms[0].length;
        Queue<int[]> queue = new LinkedList<>();
        
        // Add all gates
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (rooms[r][c] == 0) queue.offer(new int[]{r, c});
            }
        }
        
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];
            
            for (int[] d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];
                
                // If bounds, and it is an empty room (INF, represented as 2147483647)
                if (nr >= 0 && nc >= 0 && nr < rows && nc < cols && rooms[nr][nc] == Integer.MAX_VALUE) {
                    rooms[nr][nc] = rooms[r][c] + 1;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
    }
}
```

---

## 03. Word Ladder

**In My Words:** Given two words, `beginWord` and `endWord`, and a `wordList`, find the length of the shortest transformation sequence from `begin` to `end`. A transformation means changing exactly 1 letter at a time, and every intermediate word must be in the `wordList`.

**Constraint Whispers:**
- Shortest path = Graph BFS.
- But we aren't given a graph... we have to build it implicitly!

**The Bridge:** How do we find neighbors for a word like `"hot"`? 
Option A: Compare `"hot"` to every word in the dictionary ($O(N \cdot L)$ per word). Slow if dictionary is huge.
Option B: Replace each character in `"hot"` with 'a' through 'z' and check if that generated word exists in the dictionary! ($O(L \cdot 26)$ per word). Much faster!

**Optimized Intuition:**
1. Put all words in a `HashSet` for $O(1)$ lookups. If `endWord` not in set, return 0.
2. Initialize Queue. Enqueue `beginWord`. Initialize `steps = 1`.
3. BFS loop. For each word in queue:
   - If `word.equals(endWord)` return `steps`.
   - Generate all 26 variants for each of the $L$ characters.
   - If variant is in HashSet: enqueue it, and IMMEDIATELY remove it from the HashSet (the HashSet acts as our `visited` set to prevent cycles and guarantees shortest path).
4. After `size` loop, `steps++`.

**Time:** $O(M^2 \cdot N)$ where M is word length | **Space:** $O(M \cdot N)$ for Queue/Set

**Code Solution:**
```java
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> dict = new HashSet<>(wordList);
        if (!dict.contains(endWord)) return 0;
        
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        
        int steps = 1;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            
            for (int i = 0; i < size; i++) {
                String curr = queue.poll();
                if (curr.equals(endWord)) return steps;
                
                // Generate all possible 1-char edits
                char[] chars = curr.toCharArray();
                for (int j = 0; j < chars.length; j++) {
                    char original = chars[j];
                    
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == original) continue;
                        chars[j] = c;
                        String nextWord = new String(chars);
                        
                        // If it's a valid dictionary word
                        if (dict.contains(nextWord)) {
                            queue.offer(nextWord);
                            dict.remove(nextWord); // Mark visited
                        }
                    }
                    chars[j] = original; // Backtrack character
                }
            }
            steps++;
        }
        
        return 0; // No path found
    }
}
```
