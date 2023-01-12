from collections import defaultdict, Counter
def countSubTrees(n, edges, labels):
    graph = defaultdict(list)
    ans = [0 for _ in range(n)]
    visited = set()
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)
    def dfs(node):
        if node in visited:
            return Counter()
        visited.add(node) 
        count = Counter()
        count[labels[node]] += 1
        for node2 in graph[node]:
            count += dfs(node2)
        ans[node] = count[labels[node]]
        return count
    dfs(0)
    return ans