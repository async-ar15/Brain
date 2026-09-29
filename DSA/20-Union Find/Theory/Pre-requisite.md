# 20. Union Find - Pre-requisites

## Disjoint Set (Union-Find) Data Structure

The Union-Find data structure (also known as Disjoint Set) is a powerful tool specifically designed to keep track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.

It answers two fundamental questions in near $O(1)$ time:
1. **Find:** Which subset does element `A` belong to? (Usually returns the "root" or "representative" of the subset).
2. **Union:** Merge the subset containing `A` with the subset containing `B`.

## Why not just use DFS/BFS?

DFS and BFS are great for finding Connected Components when the entire graph is known upfront (a static graph).
However, if edges are being added *dynamically* over time, running a full DFS every time a new edge is added to check if two nodes are connected takes $O(V+E)$ per edge.

Union-Find handles dynamic connectivity in amortized $O(\alpha(N))$ time, which is practically $O(1)$.

## The Intuition: Trees and Roots

Imagine each subset as a Tree.
- Initially, every node is its own tree root.
- To `Union(A, B)`, we find the root of `A`'s tree, find the root of `B`'s tree, and make one root point to the other.
- To `Find(A)`, we traverse up parent pointers until we hit a node that points to itself (the root). If `Find(A) == Find(B)`, they are in the same subset!
