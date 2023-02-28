# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
class Solution:
    def shipWithinDays(self, weights, days):
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            mid = (l+r)//2
            if self.capacityOK(weights, days, mid):
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1 
        return res
    
    def capacityOK(self, weights, days, capacity):
        curr_cap = capacity
        ship = 1
        for w in weights:
            if curr_cap - w < 0:
                ship += 1
                curr_cap = capacity
            curr_cap -= w
        return ship <= days