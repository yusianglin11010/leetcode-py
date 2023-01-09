def preorderTraversal(root):
    stack = [root]
    ans = []
    while stack:
        node = stack.pop()
        if node:
            ans.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return ans