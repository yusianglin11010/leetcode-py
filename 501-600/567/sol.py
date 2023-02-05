# https://leetcode.com/problems/permutation-in-string/description/
def checkInclusion(s1, s2):
    d = {}
    for w in s1:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    k = len(s1)
    matched = 0
    for i in range(len(s2)):
        if s2[i] in d:
            d[s2[i]] -= 1
            if d[s2[i]] == 0:
                matched += 1
        if i >= k and s2[i-k] in d:
            if d[s2[i-k]] == 0:
                matched -= 1
            d[s2[i-k]] += 1
        if matched == len(d):
            return True
    return False
