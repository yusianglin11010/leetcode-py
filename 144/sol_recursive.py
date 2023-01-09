def preorderTraversal(root):
    ans = []
    def traverse(root, ans):
        if not root:
            return
        ans.append(root.val)
        traverse(root.left, ans)
        traverse(root.right, ans)
    traverse(root, ans)
    return ans