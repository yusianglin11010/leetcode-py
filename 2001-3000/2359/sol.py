# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
from collections import defaultdict
def closestMeetingNode(edges, node1, node2):
    dist = defaultdict(list)
    def dfs(node, arr, step):
        while arr[node]==-1 and node != -1:
            arr[node] = step
            dfs(edges[node], arr, step+1)
    arr1 = [-1 for _ in range(len(edges))]
    arr2 = [-1 for _ in range(len(edges))]
    dfs(node1, arr1, 0)
    dfs(node2, arr2, 0)
    ans = -1
    res = float("inf")
    for i in range(len(edges)):
        if arr1[i] != -1 and arr2[i] != -1:
            max_dist = max(arr1[i], arr2[i])
            if max_dist < res:
                res = max_dist
                ans = i
    return ans