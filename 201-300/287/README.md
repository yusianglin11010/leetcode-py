# 287. Find the Duplicate Number

Review1: January 12, 2023
Tags: Math
URL: https://leetcode.com/problems/find-the-duplicate-number/description/

## Question

---

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return *this repeated number*.

You must solve the problem **without** modifying the array `nums` and uses only constant extra space.

**Example 1:**

```
Input: nums = [1,3,4,2,2]
Output: 2

```

**Example 2:**

```
Input: nums = [3,1,3,4,2]
Output: 3

```

**Constraints:**

- `1 <= n <= 105`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

**Follow up:**

- How can we prove that at least one duplicate number must exist in `nums`?
- Can you solve the problem in linear runtime complexity?

## Idea

---

- mod
    - use mod to count the number’s occurrence in an array
- marked visited number’s index
    - when visited a number, we marked `nums[number]` as visited by make `nums[number]` = `-nums[number]`
    - when next time we see the same number, just check the idx if there is marked as negative or not
    - note that every time we visit the element, we need to take the `abs` of this element to access `nums[number]`
- index sort
    - the key of index sort is to make every index represent its number
    - for example, if the `nums` is [2,3,1,2], then we need to make [2,3,1,2] to [3,2,1,2] in first step
    - so when we find next duplicated number, that is the last element, 2, we check `nums[2-1]` == 2, then we know that 2 is duplicated number
