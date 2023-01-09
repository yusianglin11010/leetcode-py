# 102. Binary Tree Level Order Traversal

Review1: January 9, 2023
Tags: Tree
URL: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

## Question

---

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

```

**Example 2:**

```
Input: root = [1]
Output: [[1]]

```

**Example 3:**

```
Input: root = []
Output: []

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- `1000 <= Node.val <= 1000`

## Idea

---

- deque
    - maintain a queue
        - for every while loop, we pop n time from left, while the n is the number of node in this level
- recursive
    - maintain a map to record which level has been reached
        - if not reached before, then we add a container to save the node in this level
    - for every traverse, record the level