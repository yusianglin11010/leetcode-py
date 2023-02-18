# https://leetcode.com/problems/maximum-depth-of-binary-tree/
def maxDepth( root, depth = 0):
    if not root:
        return depth
    left = maxDepth(root.left, depth+1)
    right = maxDepth(root.right, depth+1)
    return max(left, right)