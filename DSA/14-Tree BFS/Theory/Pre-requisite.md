# 14. Tree BFS - Pre-requisites

## What is BFS?

Breadth-First Search (BFS) is a traversal algorithm that explores a tree **Level by Level**.
Instead of diving as deep as possible like DFS, BFS visits the root, then ALL of the root's children (depth 1), then ALL of their children (depth 2), and so on.

## The Queue Data Structure

To implement BFS, we **CANNOT** use recursion (the Call Stack is LIFO, which forces DFS).
We must use a **Queue** (FIFO: First In, First Out).

Think of it like a waiting line:
1. The root gets in line.
2. The root is served (removed from line). Before it leaves, it puts its children in the back of the line.
3. The next person in line is served, puts their children in the back of the line, etc.

Because a Queue is FIFO, nodes at Depth 1 will always be served before nodes at Depth 2.

## Java `Queue` Implementation

In Java, `Queue` is an interface. The standard implementation you should use is `LinkedList` or `ArrayDeque`.

```java
import java.util.Queue;
import java.util.LinkedList;

Queue<TreeNode> queue = new LinkedList<>();

queue.offer(root); // Adds to the back (enqueue)
TreeNode current = queue.poll(); // Removes and returns from the front (dequeue)
int size = queue.size();
boolean isEmpty = queue.isEmpty();
```
