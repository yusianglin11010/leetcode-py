
def wordBreak(s, wordDict):
    d = set(wordDict)
    m = {}
    def dfs(s):
        if s in m:
            return m[s]
        if not s:
            return [""]
        res = []
        for i in range(1,len(s)+1):
            if s[:i] in d:
                for word in dfs(s[i:]):
                    res.append(s[:i] + (" " if word else "") + word)
        m[s] = res
        return res
    return dfs(s)
        