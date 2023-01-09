# 149. Max Points on a Line

Review1: January 8, 2023
Tags: Greedy
URL: https://leetcode.com/problems/max-points-on-a-line/

## Question

---

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane, return *the maximum number of points that lie on the same straight line*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg](https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg)

```
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg](https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg)

```
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

```

**Constraints:**

- `1 <= points.length <= 300`
- `points[i].length == 2`
- `104 <= xi, yi <= 104`
- All the `points` are **unique**.

## Idea

---

- for every node, we need to calculate the slope between it and the other nodes
    - if the slope is same, then we say they could form a line
- so all we need to do is for each node, maintain a hashtable to count the slope
    - the return value is the maximum of counting of slope