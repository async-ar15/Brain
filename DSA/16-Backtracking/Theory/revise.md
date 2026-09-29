# Backtracking — Revision Sheet

---

## 01. Subsets

**In My Words:** Given an integer array `nums` of unique elements, return all possible subsets (the power set).

**Constraint Whispers:**
- $1 \le nums.length \le 10$ (Classic backtracking constraint).

**The Bridge:** Order doesn't matter for subsets. `[1, 2]` is the same as `[2, 1]`. To prevent generating both, we strictly enforce a left-to-right selection using a `start` index. A subset can be any length, so EVERY path we explore is a valid subset!

**Optimized Intuition:** 
Base case: There isn't one! Every time the function is called, add a copy of `currentPath` to `result`.
Loop `i` from `start` to `nums.length`.
`currentPath.add(nums[i])`
`backtrack(i + 1)`
`currentPath.remove(last)`

**Template:** Combinations/Subsets (Use `start` index)

**Time:** $O(N \cdot 2^N)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), nums, 0);
        return res;
    }
    
    private void backtrack(List<List<Integer>> res, List<Integer> current, int[] nums, int start) {
        // Every node in the state-space tree is a valid subset
        res.add(new ArrayList<>(current));
        
        for (int i = start; i < nums.length; i++) {
            current.add(nums[i]);
            backtrack(res, current, nums, i + 1);
            current.remove(current.size() - 1);
        }
    }
}
```

---

## 02. Combination Sum

**In My Words:** Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of candidates where the chosen numbers sum to `target`. You may choose the same number an UNLIMITED number of times.

**The Bridge:** It's a combinations problem, so we use the `start` index to prevent duplicate sets (like `[2, 3]` and `[3, 2]`). Because we can reuse the same number, when we recurse, we DO NOT do `i + 1`. We just pass `i` again!

**Optimized Intuition:**
Base cases: If `currentSum == target`, add to result, return. If `currentSum > target`, return (dead end).
Loop `i` from `start` to `candidates.length`.
`currentPath.add(nums[i])`
`backtrack(i)` // Reuse allowed!
`currentPath.remove(last)`

**Time:** $O(N^{\frac{T}{M}})$ (Where T is target, M is min element) | **Space:** $O(\frac{T}{M})$

**Code Solution:**
```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), candidates, target, 0, 0);
        return res;
    }
    
    private void backtrack(List<List<Integer>> res, List<Integer> curr, int[] candidates, int target, int sum, int start) {
        if (sum == target) {
            res.add(new ArrayList<>(curr));
            return;
        }
        if (sum > target) {
            return;
        }
        
        for (int i = start; i < candidates.length; i++) {
            curr.add(candidates[i]);
            // Notice we pass 'i', not 'i + 1', because we can reuse the same element
            backtrack(res, curr, candidates, target, sum + candidates[i], i);
            curr.remove(curr.size() - 1);
        }
    }
}
```

---

## 03. Permutations

**In My Words:** Given an array `nums` of distinct integers, return all the possible permutations.

**The Bridge:** Order DOES matter. `[1, 2]` and `[2, 1]` are both required. Therefore, we CANNOT use a `start` index to restrict movement left-to-right. Every recursive call must loop from `i = 0` to `n`. But we can't use the *exact same element* twice in a permutation (no `[1, 1]`), so we need a `visited` array (or `if (current.contains(nums[i]))` if array is distinct).

**Optimized Intuition:**
Base case: `currentPath.size() == nums.length`. Add to result, return.
Loop `i` from `0` to `nums.length`.
If `visited[i] == true`, continue.
`visited[i] = true`, `currentPath.add(nums[i])`.
`backtrack()`
`visited[i] = false`, `currentPath.remove(last)`.

**Template:** Permutations (No `start` index, use `visited` array)

**Time:** $O(N \cdot N!)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), nums, new boolean[nums.length]);
        return res;
    }
    
    private void backtrack(List<List<Integer>> res, List<Integer> curr, int[] nums, boolean[] visited) {
        if (curr.size() == nums.length) {
            res.add(new ArrayList<>(curr));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) continue; // Skip elements already in the permutation
            
            visited[i] = true;
            curr.add(nums[i]);
            
            backtrack(res, curr, nums, visited);
            
            visited[i] = false;
            curr.remove(curr.size() - 1);
        }
    }
}
```

---

## 04. Word Search

**In My Words:** Given an $m \times n$ grid of characters `board` and a `string` word, return true if `word` exists in the grid. The word must be constructed from sequentially adjacent cells (horizontally or vertically).

**The Bridge:** This is a DFS on a 2D grid, but with backtracking because we are searching for a specific sequence. If we go down a path and the next letter doesn't match, we must "undo" our steps so those cells can be used by a different, potentially successful path.

**Optimized Intuition:**
Loop through every cell in the grid. If `board[r][c] == word.charAt(0)`, start `dfs`.
`dfs(r, c, index)`:
Base case 1: `index == word.length()` return true.
Base case 2: Out of bounds, or `board[r][c] != word.charAt(index)`, or cell visited -> return false.
Mark visited (trick: `board[r][c] = '#'`).
Recursive call 4 directions. If any returns true, return true.
Backtrack: restore cell `board[r][c] = word.charAt(index)`.

**Time:** $O(M \cdot N \cdot 4^L)$ where L is word length | **Space:** $O(L)$

**Code Solution:**
```java
class Solution {
    public boolean exist(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (dfs(board, r, c, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    private boolean dfs(char[][] board, int r, int c, String word, int i) {
        if (i == word.length()) return true;
        
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length || board[r][c] != word.charAt(i)) {
            return false;
        }
        
        char temp = board[r][c];
        board[r][c] = '#'; // Mark as visited
        
        boolean found = dfs(board, r + 1, c, word, i + 1) ||
                        dfs(board, r - 1, c, word, i + 1) ||
                        dfs(board, r, c + 1, word, i + 1) ||
                        dfs(board, r, c - 1, word, i + 1);
                        
        board[r][c] = temp; // Backtrack (unmark)
        
        return found;
    }
}
```
