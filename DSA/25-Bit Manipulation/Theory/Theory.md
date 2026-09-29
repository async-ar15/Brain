# Theory - Bit Manipulation

Bit Manipulation is rarely about writing complex algorithms. It's about knowing specific mathematical tricks that run in $O(1)$ time.

## Where is it commonly used?
1. **Finding single elements:** Finding a number that doesn't appear twice in an array.
2. **Counting Set Bits:** Counting how many '1's are in a binary representation.
3. **Subsets (Bitmasking):** Generating subsets using binary numbers from 0 to $2^N-1$.

## The 4 Golden Tricks of Bit Manipulation

Memorize these. They are the punchlines to almost every bit manipulation interview question.

### 1. XOR cancels itself out
`A ^ A = 0`
`A ^ 0 = A`
Order doesn't matter: `A ^ B ^ A = B`
*Use case: Find the single number in an array where every other number appears exactly twice. Just XOR everything together. The duplicates cancel out, leaving the single number!*

### 2. Check if the $i^{th}$ bit is set (1)
Create a "mask" by shifting 1 to the left $i$ times. Then AND it with the number.
If the result is NOT 0, the bit was set.
`if ((n & (1 << i)) != 0) { // bit is 1 }`

### 3. Drop the lowest set bit (n & (n - 1))
This is incredibly counterintuitive but magical. 
`n & (n - 1)` will ALWAYS flip the rightmost '1' bit in `n` to a '0'.
- `n = 10` (binary `1010`)
- `n - 1 = 9` (binary `1001`)
- `1010 & 1001 = 1000` (The rightmost 1 at the '2's place disappeared!)
*Use case: Brian Kernighan’s Algorithm to count the number of 1s (Hamming Weight) in a number efficiently. Just keep doing `n = n & (n - 1)` until `n == 0`.*

### 4. Check if a number is a Power of 2
Powers of 2 (2, 4, 8, 16) have exactly ONE '1' bit in their binary representation (`10`, `100`, `1000`, `10000`).
If we use the trick from above, dropping the lowest set bit should leave us with 0!
`boolean isPowerOfTwo = (n > 0) && (n & (n - 1)) == 0;`

# Your interview cheat code

```text
1. Are you finding a unique element among pairs? -> XOR (^)
2. Are you counting 1s? -> n & (n - 1)
3. Are you generating subsets? -> Bitmasking from 0 to 2^N - 1
```
