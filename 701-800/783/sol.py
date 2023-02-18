# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = inf
        prev = -inf
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            node = stack.pop()
            ans = min(ans, node.val - prev)
            prev = node.val
            root = node.right