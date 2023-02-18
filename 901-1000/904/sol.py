# https://leetcode.com/problems/fruit-into-baskets/
    def totalFruit(f):
        d = defaultdict(int)
        ans = l = 0
        for r, val in enumerate(f):
            if len(d) < 2 or f[r] in d:
                d[f[r]] += 1
                ans = max(ans, r-l+1)
            else:
                while len(d) >= 2 and l < len(f):
                    d[f[l]] -= 1
                    if d[f[l]] == 0:
                        del d[f[l]]    
                    l += 1              
        return ans  