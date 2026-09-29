# 15. Binary Search Trees (BST) - Pre-requisites

## What is a Binary Search Tree?

A Binary Search Tree (BST) is a specific type of Binary Tree that enforces a strict ordering property.

### The BST Property:
For EVERY node in the tree:
1. ALL nodes in its **Left Subtree** are strictly LESS than the node's value.
2. ALL nodes in its **Right Subtree** are strictly GREATER than the node's value.
3. Both the left and right subtrees must also be valid BSTs.

(Note: Some variations allow duplicates, putting them always on the left or always on the right, but standard LeetCode problems usually assume unique values).

## Why use a BST?

A perfectly balanced BST allows us to find, insert, or delete any value in $O(\log N)$ time.
It works exactly like Binary Search on an array:
- Looking for 10? Current node is 15. Since 10 < 15, we *know* 10 can only be in the left subtree. We completely ignore the right subtree, cutting our search space in half!

## In-Order Traversal Magic

The single most important property of a BST in competitive programming is:
**An In-Order Traversal (Left, Root, Right) of a valid BST will ALWAYS process the nodes in strictly increasing sorted order.**

If you ever need to validate a BST, or find the $K^{th}$ smallest element, an In-Order traversal is your best friend.
