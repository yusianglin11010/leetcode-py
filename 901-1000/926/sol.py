# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
def minFlipsMonoIncr(s):
    ones = 0
    zeros = 0
    ans = 0
    for w in s:
        if w == "1":
            ones += 1
        elif ones:
            ones -= 1
            ans += 1
    return ans