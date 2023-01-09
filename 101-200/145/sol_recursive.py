def postorderTraversal(root):
    def traverse(root, ans):
        if not root:
            return 
        traverse(root.left, ans)
        traverse(root.right, ans)
        ans.append(root.val)
    ans = []
    traverse(root, ans)
    return ans