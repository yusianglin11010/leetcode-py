# 15. 3Sum

Review1: January 9, 2023
Tags: Map, two-pointer
URL: https://leetcode.com/problems/3sum/description/

## Question

---

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1:**

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

```

**Example 2:**

```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

```

**Example 3:**

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

```

**Constraints:**

- `3 <= nums.length <= 3000`
- `105 <= nums[i] <= 105`

## Idea

---

- two pointer
    - first sorting the nums
    - for each looping, use `ith` node as left most and `i+1` as mid, and `len(nums)-1` as right most
    - calculate sum of these three nodes, and move `mid` forward or `right` backward to match the condition(summation == 0)
    - duplication handling
        - if `nums[left`] == `nums[left-1]`, skip these left most
        - if `nums[mid]` == `nums[mid+1]`, move mid forward until `nums[mid]` ≠ `nums[mid+1]`
        - if `nums[right]` == `nums[right-1]`, move right backward until `nums[right]` ≠ `nums[right-1]`
- set
    - the possible triplet could be the four condition below
        - triplet has one zero
        - triplet has three zero
        - triplet has two negative
        - triplet has two positive