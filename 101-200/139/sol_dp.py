def wordBreak(s, wordDict):
    dp = [False for _ in range(len(s)+1)]
    dp[0] = True
    for i in range(len(s)):
        if dp[i]:
            for j in range(i,len(s)+1):
                if s[i:j] in wordDict:
                    dp[j] = True
    return dp[-1] 
