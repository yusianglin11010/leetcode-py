# https://leetcode.com/problems/missing-number/description/
def missingNumber(nums):
    n = len(nums)
    res = 0
    res ^= n
    for idx, num in enumerate(nums):
        res ^= idx^num
    return res