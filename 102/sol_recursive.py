def levelOrder(self, root):
    level = set()
    ans = []
    def traverse(root, l, level, ans):
        if not root:
            return 
        if l not in level:
            ans.append([])
            level.add(l)
        ans[l].append(root.val)
        traverse(root.left, l+1, level, ans)
        traverse(root.right, l+1, level, ans)
    traverse(root, 0, level, ans)
    return ans