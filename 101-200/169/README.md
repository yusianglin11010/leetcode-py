# 169. Majority Element

Review1: January 11, 2023
Tags: Math
URL: https://leetcode.com/problems/majority-element/description/

## Question

---

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

```
Input: nums = [3,2,3]
Output: 3

```

**Example 2:**

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2

```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `109 <= nums[i] <= 109`

**Follow-up:**

Could you solve the problem in linear time and in O(1) space?

## Idea

---

- count and record the current candidate
    - record a current target
    - if now `count` == 0, then `target` = num
    - if `num` == `target`, then count+=1
    - elif `num` ≠ `target`, then count-=1
- by the above steps, we could make sure that the mode would be the target in the end
- we could imagine that the mode is 1 and the other number is -1, the summation of this array would always > 0