# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
from collections import Counter
def findAnagrams(s, p):
    d = Counter(p)
    matched = 0
    ans = []
    k = len(p)
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]] -= 1
            if d[s[i]] == 0:
                matched += 1
        if i-k >=0 and s[i-k] in d:
            if d[s[i-k]] == 0:
                matched -=1
            d[s[i-k]] += 1
        if matched == len(d):
            ans.append(i-k+1)
    return ans
        