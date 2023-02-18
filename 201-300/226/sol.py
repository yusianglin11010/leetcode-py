# https://leetcode.com/problems/invert-binary-tree/description/
def invertTree(root):
    if not root:
        return
    tmp = root.left
    root.left = self.invertTree(root.right)
    root.right = self.invertTree(tmp)     
    return root
