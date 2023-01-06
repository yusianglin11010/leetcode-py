def maxIceCream(costs, coins):
    costs.sort()
    i = 0
    ans = 0
    while i < len(costs):
        coins -= costs[i]
        if coins < 0:
            return ans
        i += 1
        ans += 1
    return ans