# 05. Binary Search - Pre-requisites

## Linear Search vs Binary Search

Imagine you have a phone book and you want to find "Smith".
- **Linear Search:** You start at page 1, read every name, turn to page 2, read every name... This is $O(N)$.
- **Binary Search:** You open the book exactly to the middle. You see "Miller". "Smith" comes after "Miller" alphabetically, so you rip the book in half, throw away the first half, and open the remaining half to the middle. This is $O(\log N)$.

**Core Requirement:** The data **MUST** be sorted (or exhibit a monotonic property) for Binary Search to work. If the phone book was completely randomized, ripping it in half wouldn't tell you which half "Smith" is in.

## Logarithmic Time Complexity: $O(\log N)$

What does $\log N$ actually mean?
It means: "How many times can you divide $N$ by 2 before you get to 1?"

- $N = 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$ (4 steps)
- $N = 1,000,000$ (1 million) $\rightarrow$ roughly 20 steps!
- $N = 1,000,000,000$ (1 billion) $\rightarrow$ roughly 30 steps!

Binary Search is incredibly fast. If you see a constraint like $N \le 10^5$ and a required time complexity of $O(\log N)$ or an explicitly huge constraint like $N \le 10^9$, it screams Binary Search.

## Basic Structure of Binary Search

You need three pointers: `left`, `right`, and `mid`.

```java
int left = 0;
int right = arr.length - 1;

// We use <= because the target might be exactly at left == right
while (left <= right) {
    // Math trick: Prevents integer overflow that can happen with (left + right) / 2
    int mid = left + (right - left) / 2;
    
    if (arr[mid] == target) {
        return mid; // Found it!
    } else if (arr[mid] < target) {
        // Target is bigger, throw away the left half
        left = mid + 1;
    } else {
        // Target is smaller, throw away the right half
        right = mid - 1;
    }
}
```
