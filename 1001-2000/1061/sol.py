def smallestEquivalentString(s1, s2, baseStr):
    uf = {}
    def union(p1, p2):
        r1, r2 = find(p1), find(p2)
        if r1 != r2:
            uf[r1] = min(r1, r2)
            uf[r2] = min(r1, r2)
    def find(p):
        uf.setdefault(p,p)
        if uf[p] == p:
            return p
        else:
            uf[p] = find(uf[p])
        return uf[p]
    for i in range(len(s1)):
        union(s1[i], s2[i])
    print(uf)
    ans = ""
    for s in baseStr:
        ans += find(s)
    return ans