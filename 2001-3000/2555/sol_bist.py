from heapq import heappop, heappush
import bisect
from collections import Counter
def maximizeWin(p, k):
    
    cnt = Counter(p)
    acc = [0]
    locs = sorted(cnt)
    for c in locs:
        acc.append(acc[-1] + cnt[c])
    print(acc)
    print(locs)
    
    # maximum coverage strating from current position
    cands = []
    res = {}
    for i, loc in enumerate(locs):
        x = bisect.bisect(locs, loc+k)
        print(x, loc+k)

        # covered prize counts
        res[loc] = acc[x] - acc[i]
        # maximum heap to store the prize counts and start position
        heappush(cands, (-res[loc], loc))
        
    # loop through each start position
    ans = 0
    print(cands)
    for i, loc in enumerate(locs):
        # the next segment should not overlap with the current end position
        while cands and cands[0][1] <= loc + k:
            heappop(cands)
        # pick the next largest segment
        if cands:
            ans = max(ans, res[loc] - cands[0][0])
        # if there is no rest, meaning we could cover till the end
        else:
            return max(ans, acc[-1] - acc[i])
        print(ans, cands)
    
    return ans

a = [1,1,2,2,3,3,5]
k = 2
maximizeWin(a, k)