# https://leetcode.com/problems/unique-paths/description/
def uniquePaths(m, n):
    dp = [1 for _ in range(n)]
    for _ in range(1, m):
        for i in range(1,n):
            dp[i] = dp[i-1]+dp[i]
    return dp[n-1]