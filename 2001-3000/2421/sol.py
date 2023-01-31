https://leetcode.com/problems/number-of-good-paths/description/
from collections import defaultdict
class UF:
    def __init__(self, n):
        self.par = list(range(n))

    def find(self, i):
        if i != self.par[i]:
            self.par[i] = self.find(self.par[i])
        return self.par[i]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.par[ra] = rb

class Solution:
    def numberOfGoodPaths(self, vals, edges):
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        val_map = defaultdict(list)
        for i, val in enumerate(vals):
            val_map[val].append(i)
        res = 0
        uf = UF(len(vals))
        for val in sorted(val_map.keys()):
            for i in val_map[val]:
                for nei in adj[i]:
                    if vals[nei] <= vals[i]:
                        uf.union(nei, i)
            count = defaultdict(int)
            for i in val_map[val]:
                count[uf.find(i)] += 1
                res += count[uf.find(i)]
        return res
