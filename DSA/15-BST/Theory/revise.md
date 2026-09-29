# BST — Revision Sheet

---

## 01. Validate Binary Search Tree

**In My Words:** Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

**The Bridge:** A node's value must not only be greater than its left child and less than its right child, it must be greater than ALL nodes in its left subtree and less than ALL nodes in its right subtree. We must pass down strict boundaries.

**Optimized Intuition:** Helper function `validate(node, min, max)`. Base case: null is true. If `node.val <= min` or `node.val >= max`, return false. Recursively check `validate(node.left, min, node.val)` AND `validate(node.right, node.val, max)`. Use `Long` boundaries to avoid integer overflow edge cases.

**Template:** Validate BST (Top-Down DFS)

**Time:** $O(N)$ | **Space:** $O(H)$

**Code Solution:**
```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    private boolean validate(TreeNode node, long min, long max) {
        if (node == null) return true;
        
        if (node.val <= min || node.val >= max) {
            return false;
        }
        
        return validate(node.left, min, node.val) && validate(node.right, node.val, max);
    }
}
```

---

## 02. Kth Smallest Element in a BST

**In My Words:** Given the `root` of a BST and an integer `k`, return the $k^{th}$ smallest value (1-indexed) of all the values of the nodes in the tree.

**Constraint Whispers:**
- You could just dump all values into a list and sort it ($O(N \log N)$), but that ignores the BST property.
- You can do this in $O(N)$ time.

**The Bridge:** An In-Order Traversal (Left, Root, Right) of a BST visits the nodes in strictly sorted ascending order. The $1^{st}$ node visited is the smallest, the $2^{nd}$ is the second smallest, etc.

**Optimized Intuition:** Maintain a global `count` and `result`. Run an In-Order traversal. `dfs(node.left)`. Then increment `count`. If `count == k`, store `node.val` in `result` and return. `dfs(node.right)`.

**Gotcha:** To truly optimize, stop the recursion early once you find the answer.

**Time:** $O(H + K)$ (We stop after visiting K nodes) | **Space:** $O(H)$

**Code Solution:**
```java
class Solution {
    int count = 0;
    int result = -1;
    
    public int kthSmallest(TreeNode root, int k) {
        inorder(root, k);
        return result;
    }
    
    private void inorder(TreeNode node, int k) {
        if (node == null || count >= k) return;
        
        inorder(node.left, k);
        
        count++;
        if (count == k) {
            result = node.val;
            return;
        }
        
        inorder(node.right, k);
    }
}
```

---

## 03. Lowest Common Ancestor of a Binary Search Tree

**In My Words:** Find the lowest common ancestor (LCA) node of two given nodes in the BST. (The lowest node that has both `p` and `q` as descendants).

**The Bridge:** Because it's a BST, we can use the values to guide us. If both `p` and `q` are GREATER than the current node, their LCA *must* be in the right subtree. If both are LESS than the current node, their LCA *must* be in the left subtree. If one is greater and one is less (or one equals the current node), the current node IS the split point (the LCA)!

**Optimized Intuition:** We can do this iteratively (or recursively). Start at root. If `p.val < curr.val && q.val < curr.val`, `curr = curr.left`. If `p.val > curr.val && q.val > curr.val`, `curr = curr.right`. Else, return `curr`.

**Time:** $O(H)$ | **Space:** $O(1)$ (Iterative)

**Code Solution:**
```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode curr = root;
        
        while (curr != null) {
            if (p.val > curr.val && q.val > curr.val) {
                curr = curr.right;
            } else if (p.val < curr.val && q.val < curr.val) {
                curr = curr.left;
            } else {
                // We found the split point
                return curr;
            }
        }
        return null;
    }
}
```
