# 13. Trees - Pre-requisites

## What is a Tree?

A Tree is an undirected, connected, acyclic graph. It models hierarchical data.
- **Node:** Contains data and pointers to children.
- **Root:** The topmost node.
- **Leaf:** A node with no children.
- **Height:** Max edges from a node to a leaf.
- **Depth:** Edges from root to the node.

## Binary Trees

A Binary Tree is a tree where each node has at most **two** children (Left and Right).

### The Node Definition in Java
```java
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
```

## Traversal Types (DFS vs BFS)

To process a tree, we have to visit every node. There are two main philosophies:

1. **Depth-First Search (DFS):** Go as deep as possible down one path before backtracking. Uses a Stack (usually the recursion Call Stack).
2. **Breadth-First Search (BFS):** (Covered in Day 14). Visit all nodes at depth 1, then depth 2, etc. Uses a Queue.

## The 3 DFS Orderings

When doing DFS, you visit a node, go left, and go right. The *order* in which you process the node's value defines the traversal name:

1. **Pre-order (Root, Left, Right):** Process the node BEFORE its children. Useful for copying a tree.
2. **In-order (Left, Root, Right):** Process the node BETWEEN its children. For a BST, this prints values in sorted order!
3. **Post-order (Left, Right, Root):** Process the node AFTER its children. Useful for deleting a tree, or calculating heights (because you need the children's heights before you can calculate the parent's height).

```java
// Template for recursive DFS
public void dfs(TreeNode root) {
    if (root == null) return;
    
    // System.out.println(root.val); // PRE-ORDER
    
    dfs(root.left);
    
    // System.out.println(root.val); // IN-ORDER
    
    dfs(root.right);
    
    // System.out.println(root.val); // POST-ORDER
}
```
