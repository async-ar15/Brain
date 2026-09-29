# 20. Topological Sort - Pre-requisites

## What is a DAG?

Topological Sort ONLY works on **Directed Acyclic Graphs (DAG)**.
- **Directed:** The edges have arrows (A $\rightarrow$ B means you must do A before B).
- **Acyclic:** There are no loops (You can't have A $\rightarrow$ B $\rightarrow$ C $\rightarrow$ A, otherwise you could never start!).

## Real World Analogy

Think of Topological Sort as creating a **Course Schedule** for university.
- Course A (Intro to CS) is a prerequisite for Course B (Data Structures).
- Therefore, Course A must appear BEFORE Course B in your schedule.

If you have a loop (A requires B, and B requires A), you can never graduate. This means a valid Topological Sort doesn't exist.

## In-Degree and Out-Degree

To implement the algorithm, you must understand these terms:
- **In-Degree:** The number of arrows pointing INTO a node. (How many prerequisites does this course have?)
- **Out-Degree:** The number of arrows pointing OUT OF a node. (How many advanced courses does this course unlock?)

If a node has an **In-Degree of 0**, it means it has NO prerequisites. You can take it immediately! This is the starting point of the algorithm.
