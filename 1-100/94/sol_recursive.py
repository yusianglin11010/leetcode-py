def inorderTraversal(root):
    ans = []
    def traverse(root, ans):
        if not root:
            return 
        traverse(root.left, ans)
        ans.append(root.val)
        traverse(root.right, ans)
    traverse(root, ans)
    return ans