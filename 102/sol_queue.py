def levelOrder(self, root):
    dq = deque([root])
    ans = []
    while dq:
        tmp = []
        for _ in range(len(dq)):
            node = dq.popleft()
            if node:
                tmp.append(node.val)
                dq.append(node.left)
                dq.append(node.right)
        if tmp:
            ans.append(tmp)
    return ans