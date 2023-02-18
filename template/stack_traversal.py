class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Template
def traversal(root):
    stack, ans = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return ans
        node = stack.pop()
        root = node.right



def traversal(root):
    stack, ans = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return ans
        node = stack.pop()
        # we append node here for inorder traversal
        # this step is when we have already visited one node and going leave it
        ans.append(node.val)
        root = node.right

def traversal_preorder(root):
    stack, ans = [], []
    while True:
        while root:
            stack.append(root)
            # we append node here for preorder traversal
            # here is the first time we visit the node
            ans.append(root.val)
            root = root.left
        if not stack:
            return ans
        node = stack.pop()
        root = node.right


def traversal_postorder(root):
    stack, ans = [], []
    while True:
        while root:
            stack.append((root, 2))
            stack.append((root, 1))
            root = root.left
        if not stack:
            return ans
        node, seen = stack.pop()
        if seen = 2:
            ans.append(node.val)
        # for the first time we visit the node, we first go to its right
        else:
            root = node.right