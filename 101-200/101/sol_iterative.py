# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSymmetric(root: Optional[TreeNode]):
    stack = [(root.left, root.right)]
    while stack:
        left, right = stack.pop()
        if not left and not right:
            continue
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        stack.append((left.left, right.right))
        stack.append((left.right, right.left))
    return True