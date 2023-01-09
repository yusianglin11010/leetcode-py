def preorderTraversal(root):
    stack, ans = [], []
    while True:
        while root:
            ans.append(root.val)
            stack.append(root)
            root = root.left
        if not stack:
            return ans
        node = stack.pop()
        root = node.right