# https://leetcode.com/problems/single-number/
def singleNumber(nums):
    return 2*sum(set(nums)) - sum(nums)