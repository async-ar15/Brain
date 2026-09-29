# 24. Bit Manipulation - Pre-requisites

## Binary Numbers

At the hardware level, everything is 1s and 0s. 
In a 32-bit integer, the number 5 is represented as:
`00000000 00000000 00000000 00000101`

Each position represents a power of 2:
`... 16  8  4  2  1`
`     0  0  1  0  1` -> $4 + 1 = 5$

## Bitwise Operators

1. **AND (`&`)**: 1 if BOTH bits are 1.
   - `1010 & 1100 = 1000`
2. **OR (`|`)**: 1 if EITHER bit is 1.
   - `1010 | 1100 = 1110`
3. **XOR (`^`)**: 1 if bits are DIFFERENT.
   - `1010 ^ 1100 = 0110`
4. **NOT (`~`)**: Flips all bits.
   - `~1010 = 0101` (Note: In Java, this applies to all 32 bits, making it a negative number due to Two's Complement).
5. **Left Shift (`<<`)**: Shifts bits left, fills right with 0. Mathematically multiplies by 2.
   - `1010 << 1 = 10100`
6. **Right Shift (`>>`)**: Shifts bits right, keeps the sign bit. Mathematically divides by 2.
   - `1010 >> 1 = 0101`

## The Two's Complement System (Negative Numbers)

How does a computer represent `-5`? It uses Two's Complement.
1. Take the positive representation of 5: `00000101`
2. Invert all the bits (NOT): `11111010`
3. Add 1 to the result: `11111011`

The leftmost bit (Sign Bit) is 1, indicating a negative number.
