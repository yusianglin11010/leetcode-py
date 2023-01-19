# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
def subarraysDivByK(A, K):
    res = 0
    prefix = 0
    count = [1] + [0] * K
    for num in A:
        prefix = (prefix+num)%K
        res += count[prefix]
        count[prefix] += 1 # the counting of prefix means that how many times our prefix sum would cross i
    return res