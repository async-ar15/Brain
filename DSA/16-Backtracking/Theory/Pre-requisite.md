# 16. Backtracking - Pre-requisites

## What is Backtracking?

Backtracking is an algorithmic paradigm used to find all (or some) solutions to a computational problem incrementally. It builds candidates for the solution and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Think of it like exploring a maze:
1. You take a path.
2. You hit a dead end (or reach the goal and record it).
3. You **walk back** (backtrack) to the last intersection and try a different path.

## The Difference Between DFS and Backtracking

Backtracking is essentially Depth-First Search (DFS) applied to a "State Space Tree" rather than a physical graph/tree structure.
- **DFS:** Exploring existing nodes in a tree/graph.
- **Backtracking:** *Generating* the nodes of a conceptual tree of choices, and "undoing" choices to explore other branches.

## Combinatorics 101

Backtracking is the standard way to solve combinatorial problems. You must understand the difference:
1. **Permutations:** Order matters. `[1, 2]` is different from `[2, 1]`.
2. **Combinations/Subsets:** Order DOES NOT matter. `[1, 2]` is the same as `[2, 1]`.

## The State Problem (Why we "Undo")

In Backtracking, we often use a single data structure (like a Java `List` or `StringBuilder`) to represent our "current path".
Because objects are passed by *reference* in Java, if we modify the list in one branch of the recursion, those modifications will persist when we return to the parent.
Therefore, we MUST explicitly "undo" our choice (remove the last element) after the recursive call returns, to ensure the next branch starts with a clean slate.
