def threeSum(nums):
    p, n, z = [], [], []
    ans = set()
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)
    P, N = set(p), set(n)
    if len(z) > 0:
        for num in P:
            if -1*num in N:
                ans.add((0,num, -1*num))
    if len(z) >= 3:
        ans.add((0,0,0))
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            target = -1 * (p[i]+p[j])
            if target in N:
                ans.add(tuple(sorted([p[i], p[j], target])))
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            target = -1 * (n[i]+n[j])
            if target in P:
                ans.add(tuple(sorted([n[i], n[j], target])))
    return ans