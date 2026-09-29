# Theory - Backtracking

Backtracking problems follow an extremely rigid template. Once you memorize the structure, these problems become mechanical.

## Where is it commonly used?
1. Generating Subsets, Permutations, Combinations.
2. Exploring all valid paths (e.g., Word Search, N-Queens, Sudoku Solver).

## Strong signals to look for
- "Find **all** possible combinations..."
- "Return **all** permutations..."
- $N$ is incredibly small (e.g., $N \le 12$). Backtracking algorithms are inherently exponential $O(2^N)$ or factorial $O(N!)$, so a small constraint is a dead giveaway.

## The Universal Backtracking Template

Every backtracking function needs 3 things:
1. **The Choice:** What are the options at this step? (Often a `for` loop).
2. **The Constraints:** Is this choice valid?
3. **The Goal (Base Case):** Have we reached a complete solution?

```java
public void backtrack(List<List<Integer>> result, List<Integer> currentPath, int[] nums, int start) {
    // 1. Goal (Base Case)
    if (isGoal(currentPath)) {
        // ALWAYS ADD A DEEP COPY OF THE PATH!
        result.add(new ArrayList<>(currentPath)); 
        return; // Sometimes we return, sometimes we don't (like in Subsets)
    }
    
    // 2. Explore Choices
    for (int i = start; i < nums.length; i++) {
        // (Optional) Constraints: Skip invalid choices
        if (!isValid(nums[i])) continue;
        
        // 3. Make the Choice (DO)
        currentPath.add(nums[i]);
        
        // 4. Explore further (RECURSE)
        backtrack(result, currentPath, nums, i + 1); // Or i, depending on if reuse is allowed
        
        // 5. Undo the Choice (UNDO / BACKTRACK)
        currentPath.remove(currentPath.size() - 1);
    }
}
```

## Crucial Rule: The Deep Copy
Notice `result.add(new ArrayList<>(currentPath));`
If you just do `result.add(currentPath)`, you are adding a *reference* to the list. Since you keep modifying `currentPath` and eventually empty it out via backtracking, your final `result` list will just contain a bunch of empty lists! You must create a new object snapshot.

## Controlling Duplicates / Permutations vs Subsets

- **Permutations:** You want `[1,2]` and `[2,1]`. So your `for` loop ALWAYS starts at `i = 0`. You must use a `boolean[] visited` array to avoid picking the exact same element twice in one path.
- **Subsets / Combinations:** You DO NOT want `[2,1]`. Order must be strictly left-to-right to avoid duplicates. So your `for` loop starts at `i = start`.

# Your interview cheat code

```text
1. Does it ask for ALL possible ways/combinations?
                  ↓
2. Is N very small (N < 20)?
                  ↓
           BACKTRACKING (DO -> RECURSE -> UNDO)
```
