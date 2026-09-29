# 02. Two Pointers - Pre-requisite

## 1. Arrays and Pointers

An array is a collection of items stored at contiguous (side-by-side) memory locations. Because they are stored next to each other, the computer can instantly calculate where any item is if it knows the starting address.

A **Pointer** in this context isn't a low-level C memory pointer, but rather an **index variable** (`left = 0`, `right = arr.length - 1`) that we use to point to specific elements in the array.

Key Characteristics:
- We can randomly access any element via its index in $O(1)$ time.
- Moving a pointer left or right by one position is $O(1)$ time.

## 2. Strings and Mutability

A string is essentially an array of characters. The concepts are almost identical to arrays, but with one massive catch in many programming languages: Immutability.

- **Immutable** (Java, Python, C#, JS): Once a string is created, you cannot change it.
- **Mutable** (C, C++): Strings can be changed in-place like normal arrays.

When using Two Pointers on strings in Java, we usually convert them to a `char[]` array first to allow in-place swapping.

## Code snippets (Java)

```java
// --- CONVERTING STRING TO CHAR ARRAY ---
String s = "hello";
char[] charArray = s.toCharArray(); // O(N) Time and Space
charArray[0] = 'H'; // Modify in place

// --- SWAPPING TWO ELEMENTS ---
// Very common in Two Pointers (e.g., reversing an array)
int left = 0;
int right = charArray.length - 1;

char temp = charArray[left];
charArray[left] = charArray[right];
charArray[right] = temp;

// --- REBUILDING STRING ---
String result = new String(charArray); // O(N) Time and Space
```
