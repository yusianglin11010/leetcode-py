# 41. First Missing Positive

Review1: January 9, 2023
Tags: Map, Math
URL: https://leetcode.com/problems/first-missing-positive/description/

## Question

---

Given an unsorted integer array `nums`, return the smallest missing positive integer.

You must implement an algorithm that runs in `O(n)` time and uses constant extra space.

**Example 1:**

```
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

```

**Example 2:**

```
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

```

**Example 3:**

```
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

```

**Constraints:**

- `1 <= nums.length <= 105`
- `231 <= nums[i] <= 231 - 1`

## Idea

---

- set, O(n) times O(n) space
    - add all number to a set
    - from 1 to 2^31-1, search if exist in set
- mod, O(n) times and O(1) space
    - the minimum missing positive could only be in `[1, len(num)+1]`
    - use `nums[nums[i]%n]+=n` to count result and save the result in original array
    - if array do not have `i`, then we could know that by check `nums[i] // n  == 0` because `nums[i]` have never been added any number in counting step
        - because in the first for loop we change all values which less than 1 or greater than `len(num)+1`, so we could promise that the `nums[i]//n` could denote as the occurrences of `i`