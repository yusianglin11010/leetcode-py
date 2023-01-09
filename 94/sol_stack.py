def inorderTraversal(root):
    stack, ans = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return ans
        node = stack.pop()
        ans.append(node.val)
        root = node.right