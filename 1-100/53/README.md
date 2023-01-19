# 53. Maximum Subarray

Review1: January 18, 2023
Tags: DP
URL: https://leetcode.com/problems/maximum-subarray/description/

## Question

---

Given an integer array `nums`, find thesubarray with the largest sum, and return *its sum*.

**Example 1:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

```

**Example 2:**

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

```

**Example 3:**

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

```

**Constraints:**

- `1 <= nums.length <= 105`
- `104 <= nums[i] <= 104`

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## Idea

---

- Kadane’s algorithm
    - all we need is to maintain `total_max` to record the answer and the `current_max` to record the maximum subarray from array[0:i]
    - the maintaining of `total_max` is to compare the `current_max` to `total_max` for every iteration
    - the maintaining of `current_max` is to determine if the `current_max` is reset to `nums[i]` or `current_max` + `nums[i]`
- DP
    - maintain a dp table, where dp[i] is the maximum of subarray of `array[0:i]`
    - to maintain this dp table, we only need to determine for every `dp[i]`, if we plus nums[i] to dp[i-1] or not
        - `dp[i] = max(dp[i-1]+nums[i], nums[i])`