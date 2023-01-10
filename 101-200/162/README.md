# 162. Find Peak Element

Review1: January 10, 2023
Tags: Binary Search
URL: https://leetcode.com/problems/find-peak-element/description/

## Question

---

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

**Example 2:**

```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `231 <= nums[i] <= 231 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

## Idea

---

- use binary search
- there are three conditions after we find a mid
    - the mid itself is peak
    - the upward slope, `mid+1` > `mid`, then we could search the right side for peak, if the right side is strictly increasing, then we will find peak at last point
    - the downward slope, `mid-1` < `mid`, then we could search the left side
    - note that the neighbors number would never be the same
    - add another else condition if we found local minimum
        - e.g. [5,4,3,2,1], mid might stuck in 3