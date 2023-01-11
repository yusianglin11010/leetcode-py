# 78. Subsets

Review1: January 11, 2023
Tags: Backtrack
URL: https://leetcode.com/problems/subsets/description/

## Question

---

Given an integer array `nums` of **unique** elements, return *all possible*

*subsets*

*(the power set)*

.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

```

**Example 2:**

```
Input: nums = [0]
Output: [[],[0]]

```

**Constraints:**

- `1 <= nums.length <= 10`
- `10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

## Idea

---

- backtrack
    - maintain an `array` and go through all element
    - pop element from `array` while returning from function
- iterate
    - initialize an array with [[]]
    - go through element, and add the new element to existed subset element
        1. e.g. the first element is 1, then we could get [ [], [1] ]
        2. if the second element is 2, then we could get [ [], [1], [2], [1,2] ]
