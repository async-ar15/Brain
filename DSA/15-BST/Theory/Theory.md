# Theory - Binary Search Trees (BST)

BST problems are a hybrid of Tree problems (DFS/Recursion) and Binary Search (cutting the search space in half).

## Where is it commonly used?
1. **Searching:** Find an element, find the closest element.
2. **Validation:** Check if a tree is a valid BST.
3. **Sorted operations:** $K^{th}$ smallest, Successor/Predecessor.
4. **Lowest Common Ancestor:** Finding the splitting point of two paths.

## Strong signals to look for
- The problem explicitly states the tree is a "Binary Search Tree" or "BST".
- "Find the $K^{th}$ smallest/largest element."
- "Validate if the tree is sorted."

## Template 1: BST Search (O(log N))

Because of the BST property, we rarely need to search BOTH the left and right subtrees. We choose one path.

```java
public TreeNode searchBST(TreeNode root, int val) {
    if (root == null || root.val == val) return root;
    
    // Notice the return! We don't need to check both sides.
    if (val < root.val) {
        return searchBST(root.left, val);
    } else {
        return searchBST(root.right, val);
    }
}
```

## Template 2: Validate BST (Top-Down DFS)

You cannot validate a BST by just checking if `left < root` and `right > root` for each node.
Why? Because a right child could be greater than its parent, but LESS than the grandparent! (Which violates the rule that ALL nodes in the right subtree must be greater than the root).

**The Trick:** We must pass down a "valid range" (Min and Max bounds) for every node.

```java
public boolean isValidBST(TreeNode root) {
    // We use Long to avoid Integer.MIN_VALUE / MAX_VALUE edge cases
    return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
}

private boolean validate(TreeNode node, long min, long max) {
    if (node == null) return true;
    
    // Check if the current node violates the inherited boundaries
    if (node.val <= min || node.val >= max) {
        return false;
    }
    
    // Left child MUST be strictly less than current node's value (new max)
    // Right child MUST be strictly greater than current node's value (new min)
    return validate(node.left, min, node.val) && 
           validate(node.right, node.val, max);
}
```

# Your interview cheat code

```text
1. Is it a Binary Search Tree?
                  ↓
2. Do you need sorted order? (Use In-Order Traversal)
                  ↓
3. Do you need to find an element? (Use Binary Search logic, O(log N))
                  ↓
4. Are you validating? (Pass Min/Max boundaries top-down)
```
