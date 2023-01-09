def postorderTraversal(root):
    stack, ans = [root], []
    while stack:
        node = stack.pop()
        if node:
            ans.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return ans[::-1]