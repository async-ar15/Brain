# 11. Intervals - Pre-requisites

## What is an Interval?

An interval is essentially a range defined by a `start` and an `end` point. In Java, it is usually represented as a 2D array: `int[][] intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};`
Here, `[1, 3]` is an interval starting at 1 and ending at 3.

## The Concept of Overlapping

Two intervals overlap if the `start` of one interval is strictly less than or equal to the `end` of the previous interval.

Imagine Interval A `[startA, endA]` and Interval B `[startB, endB]`.
If we know for a fact that `startA <= startB` (because we sorted them), then they overlap if and only if:
`startB <= endA`

- Example: `[1, 3]` and `[2, 6]`. `startB` (2) is $\le$ `endA` (3). They overlap!
- Example: `[1, 3]` and `[4, 6]`. `startB` (4) is NOT $\le$ `endA` (3). No overlap.

## Sorting is Mandatory

Almost all interval problems require you to sort the intervals by their **start time** first. If you don't sort them, you would have to compare every interval with every other interval ($O(N^2)$). By sorting them by start time ($O(N \log N)$), you can process them sequentially in a single pass ($O(N)$).

### How to sort a 2D array in Java
```java
// Sort by the 0th index (start time) in ascending order
Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
```
