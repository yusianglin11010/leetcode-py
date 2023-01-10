# 215. Kth Largest Element in an Array

Review1: January 10, 2023
Tags: Sort
URL: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

## Question

---

Given an integer array `nums` and an integer `k`, return *the* `kth` *largest element in the array*.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

You must solve it in `O(n)` time complexity.

**Example 1:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

```

**Example 2:**

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

```

**Constraints:**

- `1 <= k <= nums.length <= 105`
- `104 <= nums[i] <= 104`

## Idea

---

- bucket sort
    - construct a bucket array to save the count result
    - all value - minimum number that we could do the index transform
    - if minimum number is 1, then we say that the `nums[1-1]` would be used to save `count(1)`
- quick select
    - pick a pivot
    - construct three kind of array
        - x > pivot as L
        - x < pivot as R
        - x == pivot as M
    - if k ≤ L, then we search kth largest element in L
    - if k - L - M > 0, then we search kth largest element in R
    - else kth largest must in M, we could just return M[0] with all element in M is the same
- quick select space optimization
    - do in-place swap to save the information of `x > pivot` and `x < pivot`
    - 