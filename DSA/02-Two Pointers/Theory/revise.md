# Two Pointers — Revision Sheet

---

## 01. Valid Palindrome

**In My Words:** Given a string, return true if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Constraint Whispers:**
- $O(1)$ extra space preferred.

**Brute Force:** Create a new string with only alphanumeric lowercase chars. Reverse it and compare. $O(N)$ time, $O(N)$ space.

**The Bridge:** A palindrome is mirrored. If we compare the first and last characters, they must match. We don't need a new string, just pointers moving from outside in.

**Optimized Intuition:** Left pointer at 0, right pointer at length - 1. Skip non-alphanumeric chars. Compare. If different, return false.

**Template:** Opposite Direction

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            
            left++;
            right--;
        }
        return true;
    }
}
```

---

## 02. Two Sum II

**In My Words:** Given a 1-indexed SORTED array, find two numbers that sum to target. Constant space.

**Constraint Whispers:**
- Array is sorted.
- Constant extra space ($O(1)$).

**The Bridge:** Sorting gives monotonicity. Too small? Move left pointer up. Too big? Move right pointer down.

**Optimized Intuition:** Left at 0, right at end. Compare sum to target.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) {
                return new int[]{left + 1, right + 1};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[]{};
    }
}
```

---

## 03. 3Sum

**In My Words:** Find all unique triplets that sum to zero.

**Constraint Whispers:**
- No duplicates allowed in output.
- $N \le 3000$ → $O(N^2)$ is optimal.

**The Bridge:** 3Sum is just Two Sum II inside a loop. If we sort the array and fix one number `A`, the problem becomes finding two numbers that sum to `-A`.

**Optimized Intuition:** Sort the array. For each index `i`, set `left = i + 1`, `right = end`. Run Two Sum II. Skip duplicates of `nums[i]` and duplicates inside the Two Sum loop to avoid duplicate triplets.

**Time:** $O(N^2)$ | **Space:** $O(1)$ or $O(N)$ for sorting

**Code Solution:**
```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            
            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    while (left < right && nums[left] == nums[left-1]) left++;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return res;
    }
}
```

---

## 04. Container With Most Water

**In My Words:** Given an array of heights, find two lines that together with the x-axis form a container that holds the most water.

**The Bridge:** Area = `width * min(height)`. If we start with the maximum width (pointers at the ends), the only way to increase the area is to find a taller line. So we move the pointer pointing to the SHORTER line.

**Optimized Intuition:** Left at 0, right at end. Calculate area, update max. Move whichever pointer has the smaller height inward.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;
        
        while (left < right) {
            int currentArea = Math.min(height[left], height[right]) * (right - left);
            maxArea = Math.max(maxArea, currentArea);
            
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }
}
```
