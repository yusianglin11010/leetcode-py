# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSymmetric(root):
    def traverse(node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        left = traverse(node1.right, node2.left)
        right = traverse(node1.left, node2.right)
        return left and right and node1.val == node2.val
    return traverse(root.left, root.right)
