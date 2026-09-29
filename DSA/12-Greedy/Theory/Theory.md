# Theory - Greedy

Greedy algorithms are often intuitive to think of, but very hard to prove correct. If an $O(N)$ solution feels "too simple," and $O(N^2)$ DP would TLE, it's likely a Greedy problem.

## Where is it commonly used?
1. **Maximum/Minimum problems without overlapping subproblems:** If choosing X doesn't restrict your ability to choose Y in a complex way, it might be greedy.
2. **Intervals:** Many interval problems (like Non-overlapping Intervals) are fundamentally Greedy.
3. **Jump Games:** Reaching the end of an array with variable jump lengths.
4. **Task Scheduling:** Minimizing idle time.

## The "Running Max/Min" Pattern (Jump Game)

Instead of simulating every possible path (which is exponential), you just keep track of the "farthest" you can possibly reach at any given moment. 

If the furthest you can reach eventually passes the target, you win. If you reach an index that is *beyond* your furthest reach, you lose.

### Template: Jump Game (Reachability)

```java
public boolean canReachEnd(int[] nums) {
    int maxReach = 0;
    
    for (int i = 0; i < nums.length; i++) {
        // If we arrived at an index we can't possibly reach, we fail.
        if (i > maxReach) {
            return false;
        }
        
        // Update the furthest we can reach from this new index
        maxReach = Math.max(maxReach, i + nums[i]);
        
        // Early exit if we can already reach the end
        if (maxReach >= nums.length - 1) {
            return true;
        }
    }
    
    return true;
}
```

## The "Process from the Back" Trick

Sometimes, making a greedy choice from left-to-right is difficult because you don't know the future. But if you iterate from right-to-left, the "future" becomes the "past", and the greedy choice becomes obvious.

**Example:** Jump Game can also be solved right-to-left by keeping track of the "goal post". If `index + max_jump >= goal`, the new goal becomes `index`. If the goal reaches 0, you win.

# Your interview cheat code

```text
1. Does it ask for max/min, but DP would TLE (N > 10^4)?
                  ↓
2. Can you sort the data to make an "obvious" best choice?
                  ↓
3. Does making that choice completely resolve that step without complex future consequences?
                  ↓
           GREEDY ALGORITHM (O(N) or O(N log N))
```
