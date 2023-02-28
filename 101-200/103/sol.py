# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
from collections import deque
def zigzagLevelOrder(root):
    ans = []
    q = deque()
    q.append(root)
    right = -1
    while q:
        tmp = []
        for _ in range(len(q)):
            if right == 1:
                node = q.popleft()
                if not node: continue
                q.append(node.right)
                q.append(node.left)
            else:
                node = q.pop()
                if not node: continue
                q.appendleft(node.left)
                q.appendleft(node.right)
            tmp.append(node.val)
        if tmp: ans.append(tmp)
        right *= -1
    return ans
