# 94. Binary Tree Inorder Traversal

Review1: December 7, 2022
Tags: Stack
URL: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

## Question

---

Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```
Input: root = [1,null,2,3]
Output: [1,3,2]

```

**Example 2:**

```
Input: root = []
Output: []

```

**Example 3:**

```
Input: root = [1]
Output: [1]

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `100 <= Node.val <= 100`

## Idea

---

- Recursive
    - just append value between traverse left node and right node
- Stack
    - we have to kind of node
        - node in stack
        - root node
    - the root node is the tree node and every right node
    - for root node, we need to go to its left most and append all traversing node to stack
    - we need to go back if the root is None, namely the right node is None
        - while go back, we append the `node in stack` to the answer