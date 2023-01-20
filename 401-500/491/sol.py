# https://leetcode.com/problems/non-decreasing-subsequences/
def findSubsequences(nums):
    ans = []
    def backtrack(nums, tmp, prev):
        if len(tmp) > 1:
            ans.append(tmp.copy())
        used = set()
        for i in range(len(nums)):
            if nums[i] in used:
                continue
            if nums[i] >= prev:
                used.add(nums[i])
                backtrack(nums[i+1:], tmp + [nums[i]], nums[i])
    backtrack(nums, [], -inf)
    return ans