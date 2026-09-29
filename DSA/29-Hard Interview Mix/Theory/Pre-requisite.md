# 29. Mock Interview 2 - Pre-requisites

## Handling Edge Cases

A major differentiator between a junior candidate and a senior candidate is how they handle edge cases *before* writing the core logic.

Before you write the meat of your algorithm, explicitly write out checks for:
- `null` inputs.
- Empty arrays/strings (`length == 0`).
- Arrays with only 1 element.
- Extremely large inputs (does it cause Integer Overflow? Should you use `long`?)
- Negative numbers (does your Sliding Window or DP handle negatives?)

## The Art of the "Dry Run"

When you finish coding, your instinct will be to say "I'm done." **Resist this urge.**

Instead, say: *"Let me trace this with an example to make sure it works."*

Pick a small, non-trivial example. 
- Do not pick `[1, 2, 3]` if the problem is about unsorted arrays. Pick `[3, 1, 2]`.
- Physically track the variables using comments or a piece of paper.
- Trace the `for` loops exactly as the computer would.
- If you find a bug, fix it calmly. Finding your own bug is a huge positive signal to the interviewer. Finding a bug *after* the interviewer points it out is a minor negative signal.
