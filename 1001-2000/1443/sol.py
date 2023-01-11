# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
from collections import defaultdict
def minTime(n, edges, hasApple):
    g = defaultdict(list)
    for n1, n2 in edges:
        g[n1].append(n2)
        g[n2].append(n1)
    visited = set()
    def dfs(node):
        if node in visited:
            return 0
        visited.add(node)
        secs = 0
        for child in g[node]:
            secs += dfs(child)
        if secs > 0:
            return 2 + secs
        return 2*hasApple[node]
    return max(dfs(0)-2, 0)