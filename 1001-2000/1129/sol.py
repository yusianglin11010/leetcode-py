def shortestAlternatingPaths(n, redEdges, blueEdges):
    r = defaultdict(list)
    b = defaultdict(list)
    for n1, n2 in redEdges:
        r[n1].append(n2)
    for n1, n2 in blueEdges:
        b[n1].append(n2)
    ans = [-1 for _ in range(n)]
    ans[0] = 0
    
    q = deque()
    q.append([0,0,None]) # 0-index to save node, 1-index to save length, 2-index to save color
    visited = set((0,None))
    
    while q:
        node, length, color = q.popleft()
        if ans[node] == -1:
            ans[node] = length
        if color != "R":
            for n2 in r[node]:
                if (n2,"R") not in visited:
                    q.append([n2, length+1, "R"])
        if color != "B":
            for n2 in b[node]:
                if (n2, "B") not in visited:
                    q.append([n2, length+1, "B"])
        visited.add((node, color))
    return ans