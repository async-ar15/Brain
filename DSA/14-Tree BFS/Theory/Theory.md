# Theory - Tree BFS (Level Order Traversal)

BFS is incredibly structured. The template for Tree BFS rarely ever changes.

## Where is it commonly used?
1. **Level Order Traversal:** Whenever a problem asks for an array of arrays representing levels (e.g., `[[1], [2, 3], [4, 5, 6]]`).
2. **Right/Left Side Views:** Finding the right-most or left-most node at every level.
3. **Shortest Path (in Unweighted Graphs):** (Covered in Graph BFS). In trees, it translates to finding the closest leaf node.

## Strong signals to look for
- "Level order"
- "Right side view" / "Left side view"
- "Shortest path to..."
- "Average value of each level"

## The Level-by-Level Template

The crucial part of Level Order Traversal is knowing *when* a level ends. 
If we just poll and offer continuously, all the levels blur together.

**The Trick:** At the very beginning of processing a level, take a "snapshot" of the queue's size. That size `K` is EXACTLY the number of nodes on the current level. We then run a `for` loop exactly `K` times. Any new children added during this loop go to the *back* of the queue, and won't be processed until the *next* level's `for` loop!

### Template: Level Order BFS

```java
public List<List<Integer>> bfsTemplate(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) return result;
    
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    
    while (!queue.isEmpty()) {
        int levelSize = queue.size(); // SNAPSHOT the size!
        List<Integer> currentLevel = new ArrayList<>();
        
        // Process ONLY the nodes that are part of this level
        for (int i = 0; i < levelSize; i++) {
            TreeNode current = queue.poll();
            currentLevel.add(current.val);
            
            // Add children to the queue for the NEXT level
            if (current.left != null) queue.offer(current.left);
            if (current.right != null) queue.offer(current.right);
        }
        
        result.add(currentLevel); // Add the completed level to result
    }
    
    return result;
}
```

# Your interview cheat code

```text
1. Does the problem ask about levels, layers, or depths?
                  ↓
2. Does it ask for the right-most / left-most element?
                  ↓
           TREE BFS (Queue + levelSize snapshot)
```
