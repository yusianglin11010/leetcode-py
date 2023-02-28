# https://leetcode.com/problems/find-duplicate-subtrees/description/
def findDuplicateSubtrees(root):
    def dfs(root):
        if not root:
            return "null"
        s = ",".join([str(root.val), dfs(root.left), dfs(root.right)])
        if len(subtree[s]) == 1:
            res.append(root)
        subtree[s].append(root)
        return s
    subtree = defaultdict(list)
    res = []
    dfs(root)
    return res