# https://leetcode.com/problems/word-pattern/
def wordPattern(self, pattern, s):
    s_arr = s.split(" ")
    if len(pattern) != len(s_arr):
        return False
    if len(set(pattern)) != len(set(s_arr)):
            return False
    d = {}
    for idx, p in enumerate(pattern):
        if p not in d:
            d[p] = s_arr[idx]
        else:
            if d[p] != s_arr[idx]:
                return False
    return True