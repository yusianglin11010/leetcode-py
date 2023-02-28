# https://leetcode.com/problems/minimum-impossible-or/description/?orderBy=most_votes
def minImpossibleOR(nums):
    s = set(nums)
    for i in range(32):
        if 2 ** i not in s:
            return 2 ** i