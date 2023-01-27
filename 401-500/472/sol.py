# https://leetcode.com/problems/concatenated-words/description/
def findAllConcatenatedWordsInADict(words):
    ans = []
    d = set(words)
    memo = {}
    def dfs(word):
        if word in memo:
            return memo[word]
        memo[word] = False
        for i in range(len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in d and suffix in d:
                memo[word] = True
            elif prefix in d and dfs(suffix):
                memo[word] = True
            elif dfs(prefix) and suffix in d:
                memo[word] = True
        return memo[word]
    for w in words:
        if dfs(w):
            ans.append(w)
    return ans