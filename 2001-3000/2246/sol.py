# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/
from heapq import nlargest
def longestPath(parent, s):
    graph = defaultdict(list)
    for child, par in enumerate(parent):
        if par >= 0:
            graph[par].append(child)
    self.res = -inf
    def dfs(i):
        candi = [0]
        for child in graph[i]:
            cur = dfs(child)
            if s[i] != s[child]:
                candi.append(cur)
        candi = nlargest(2, candi)
        self.res = max(self.res, sum(candi)+1)
        return max(candi) + 1
    dfs(0)
    return self.res