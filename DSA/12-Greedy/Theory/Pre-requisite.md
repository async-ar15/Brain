# 12. Greedy - Pre-requisites

## What is a Greedy Algorithm?

A Greedy Algorithm builds a solution piece by piece, always choosing the next piece that offers the most immediate, short-term benefit. It never reconsiders its choices.

**Analogy:** You are a thief in a vault with a backpack that can hold 10kg. You see a 5kg bar of gold and a 10kg bag of silver. 
- **Greedy approach:** "Gold is worth more per kg! I'll take the gold." (You take the 5kg gold, and have 5kg space left, but no other small items to take. Total value: $5000).
- **Optimal approach:** You take the 10kg of silver (Total value: $6000).

*Greedy doesn't always work!* It only works for specific problems where the "local optimum" mathematically guarantees the "global optimum".

## How to recognize if Greedy works?

Unfortunately, proving that a Greedy algorithm works mathematically is notoriously difficult (usually requiring exchange arguments or induction). 

In an interview context, you recognize a Greedy problem by:
1. **The Constraints:** If Dynamic Programming ($O(N^2)$ or $O(N \cdot W)$) is too slow (e.g., $N = 10^5$), the problem might require a Greedy $O(N)$ or $O(N \log N)$ approach.
2. **The "Obvious" Choice:** Does picking the largest/smallest/closest element immediately simplify the rest of the problem without negative consequences? (e.g., giving the smallest acceptable cookie to a child).

## Sorting is Usually Step 1

Because Greedy relies on making the "best" immediate choice, you almost always need to sort the data first so the "best" choices are presented to you in order.

- Sort intervals by end time (to leave maximum room for the future).
- Sort costs ascending (to buy as many items as possible).
- Sort values descending (to maximize profit quickly).
