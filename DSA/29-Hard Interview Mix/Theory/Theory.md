# Theory - Mock Interview 2 (Advanced Topics)

As you progress into the second mock interview, the problems usually get harder. You might encounter DP, Graphs, or complex Heaps.

## When you don't know the optimal solution

It is completely normal to face a problem you have never seen before and not instantly know the $O(N)$ solution.

**DO NOT sit in silence.** 

1. **State the Brute Force:** It shows you can at least solve the problem, and it establishes a baseline. 
2. **Identify the Bottleneck:** Why is the brute force slow? "It's $O(N^2)$ because I'm re-calculating the sum of the subarray every time."
3. **Use the "Space for Time" Trade-off:** Can a HashMap or Prefix Sum array solve that bottleneck? "If I pre-calculate the sums in an array, I can look them up in $O(1)$ time."

## Dealing with Hints

If the interviewer gives you a hint (e.g., *"Have you considered sorting the intervals first?"*), **listen to them.**
Do not stubbornly stick to your failing approach. Say, *"Ah, that makes sense. If I sort them, then I only need to compare adjacent intervals..."*

Interviewers want to see how you collaborate. Taking a hint and running with it shows you are coachable and a good team member.
