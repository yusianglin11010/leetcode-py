# https://leetcode.com/problems/naming-a-company/description/
def distinctNames(ideas):
    m = [set() for _ in range(26)]
    for idea in ideas:
        m[ord(idea[0]) - ord("a")].add(idea[1:])
    ans = 0
    for i in range(26):
        for j in range(i+1, 26):
            dup = len(m[i] & m[j])
            ans += 2 * (len(m[i]) - dup) * (len(m[j]) - dup)
    return ans