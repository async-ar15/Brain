# Trees — Revision Sheet

---

## 01. Invert Binary Tree

**In My Words:** Given the root of a binary tree, invert the tree, and return its root. (Left child becomes right child, and vice versa).

**The Bridge:** For any given node, to invert it, we just swap its left pointer with its right pointer. But that only does it for the root! To invert the whole tree, we must also invert the subtrees.

**Optimized Intuition:** 
Base case: if `root == null` return null.
Swap `root.left` and `root.right`.
Recursively call `invertTree(root.left)` and `invertTree(root.right)`.
Return `root`.

**Time:** $O(N)$ | **Space:** $O(H)$ (Height of tree for call stack)

**Code Solution:**
```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        
        invertTree(root.left);
        invertTree(root.right);
        
        return root;
    }
}
```

---

## 02. Maximum Depth of Binary Tree

**In My Words:** Return the maximum depth of the tree (number of nodes along the longest path from root to leaf).

**The Bridge:** If I know the max depth of the left subtree, and the max depth of the right subtree, my depth is just `1 + max(left, right)`.

**Optimized Intuition:** Post-order traversal (Bottom-Up). Base case: if `null`, return 0. Else, return `1 + Math.max(maxDepth(root.left), maxDepth(root.right))`.

**Time:** $O(N)$ | **Space:** $O(H)$

**Code Solution:**
```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
```

---

## 03. Diameter of Binary Tree

**In My Words:** The diameter of a binary tree is the length of the longest path between any two nodes. This path may or may not pass through the root. Length is number of EDGES.

**The Bridge:** The longest path that passes through a specific node is `maxDepth(left) + maxDepth(right)`. Since the global longest path could be deep down in the tree, we need to calculate this sum for EVERY node, and keep a global maximum.

**Optimized Intuition:** Create a global (or instance) variable `maxDiameter`. Create a helper DFS function that returns the *depth* of a node (just like the Max Depth problem). Inside that helper, before returning the depth, update `maxDiameter = max(maxDiameter, leftDepth + rightDepth)`.

**Time:** $O(N)$ | **Space:** $O(H)$

**Code Solution:**
```java
class Solution {
    int maxDiameter = 0;
    
    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return maxDiameter;
    }
    
    private int dfs(TreeNode root) {
        if (root == null) return 0;
        
        int left = dfs(root.left);
        int right = dfs(root.right);
        
        // Update the global diameter using the depths of left and right children
        maxDiameter = Math.max(maxDiameter, left + right);
        
        // Return the depth of the current subtree to its parent
        return 1 + Math.max(left, right);
    }
}
```

---

## 04. Balanced Binary Tree

**In My Words:** A height-balanced binary tree is one where the left and right subtrees of EVERY node differ in height by no more than 1. Return true if balanced.

**The Bridge:** Similar to Diameter. We need the height of the left and right subtrees for every node. If `abs(leftHeight - rightHeight) > 1`, the tree is unbalanced.

**Optimized Intuition:** Instead of doing a separate $O(N)$ height calculation for every node ($O(N^2)$ total), do a single Bottom-Up DFS. If a subtree is unbalanced, return `-1`. If the DFS sees a `-1` from a child, it propagates the `-1` upwards immediately.

**Time:** $O(N)$ | **Space:** $O(H)$

**Code Solution:**
```java
class Solution {
    public boolean isBalanced(TreeNode root) {
        return dfs(root) != -1;
    }
    
    private int dfs(TreeNode root) {
        if (root == null) return 0;
        
        int left = dfs(root.left);
        if (left == -1) return -1; // Fast fail
        
        int right = dfs(root.right);
        if (right == -1) return -1; // Fast fail
        
        if (Math.abs(left - right) > 1) {
            return -1; // Unbalanced
        }
        
        return 1 + Math.max(left, right);
    }
}
```

---

## 05. Same Tree

**In My Words:** Given roots of two binary trees `p` and `q`, check if they are exactly the same (same structure, same values).

**The Bridge:** Two trees are the same if: their root values are the same, AND their left subtrees are the same, AND their right subtrees are the same.

**Optimized Intuition:** Pre-order traversal. 
Base cases: If both null, return true. If one is null (but not both), return false. If values differ, return false.
Recursive step: `return isSameTree(p.left, q.left) && isSameTree(p.right, q.right)`.

**Time:** $O(N)$ | **Space:** $O(H)$

**Code Solution:**
```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;
        
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```
