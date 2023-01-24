# https://leetcode.com/problems/number-of-1-bits/description/
def hammingWeight(n):
    res = 0
    while n != 0:
        n = n & n-1
        res += 1
    return res