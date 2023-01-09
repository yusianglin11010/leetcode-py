def postorderTraversal(root):
    stack, ans = [], []
    while True:
        while root:
            stack.append((root, 2))
            stack.append((root, 1))
            root = root.left
        if not stack:
            return ans
        node, seen = stack.pop()
        if seen == 2:
            ans.append(node.val)
        else:
            root = node.right
