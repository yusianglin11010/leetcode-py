def wordBreak(s, wordDict):
    d = set(wordDict)
    memo = {}
    def dfs(s):
        if not s:
            return True
        if s in memo:
            return memo[s]
        memo[s] = False
        for i in range(1,len(s)+1):
            prefix = s[:i]
            suffix = s[i:]
            if prefix in d and suffix in d:
                memo[s] = True
            elif prefix in d and dfs(suffix):
                memo[s] = True
        return memo[s]
    return dfs(s)