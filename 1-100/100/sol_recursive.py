# https://leetcode.com/problems/same-tree/description/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)