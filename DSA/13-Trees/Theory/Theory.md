# Theory - Trees (DFS)

Recursion is the heart and soul of Tree algorithms. A tree is inherently recursive: every child node is the root of its own smaller subtree. 

## The Recursive Leap of Faith

To solve tree problems, you must stop trying to trace every single recursive call in your head. It will overwhelm you.
Instead, trust the "Recursive Leap of Faith":
1. Assume the recursive function works perfectly for the left and right subtrees.
2. Ask yourself: "If I already have the answer for the left subtree, and the answer for the right subtree, what do I do with them to get the answer for the current node?"
3. Write the Base Case (usually `if (root == null) return ...`).

## Bottom-Up vs Top-Down Recursion

### 1. Bottom-Up (Post-Order)
This is the most common pattern. The leaf nodes compute a value, return it to their parent, the parent combines the values, and returns it up the chain.
**Example:** Finding the max depth of a tree.

```java
public int maxDepth(TreeNode root) {
    // 1. Base Case
    if (root == null) return 0;
    
    // 2. Trust the recursion (Leap of Faith)
    int leftDepth = maxDepth(root.left);
    int rightDepth = maxDepth(root.right);
    
    // 3. Combine answers for the current node
    return 1 + Math.max(leftDepth, rightDepth);
}
```

### 2. Top-Down (Pre-Order)
You pass information *down* the tree from parent to child via function arguments.
**Example:** Path Sum (Is there a path from root to leaf that sums to target?)

```java
public boolean hasPathSum(TreeNode root, int currentSum) {
    if (root == null) return false;
    
    // Process current node
    currentSum -= root.val;
    
    // If it's a leaf node, check if we hit exactly 0
    if (root.left == null && root.right == null) {
        return currentSum == 0;
    }
    
    // Pass the state down to children
    return hasPathSum(root.left, currentSum) || hasPathSum(root.right, currentSum);
}
```

## Common Tricks
- **Same Tree / Subtree:** Recursively check if `p.val == q.val`, then `isSame(p.left, q.left)` and `isSame(p.right, q.right)`.
- **Inverting a Tree:** Swap `root.left` and `root.right`, then recursively invert the children.

# Your interview cheat code

```text
1. Can I solve this by answering the question for the left child and right child first?
                  ↓
           USE POST-ORDER (Bottom-Up)
           
2. Do I need to pass state from the root downwards to the leaves?
                  ↓
           USE PRE-ORDER (Top-Down with parameters)
```
