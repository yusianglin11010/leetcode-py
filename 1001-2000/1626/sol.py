def bestTeamScore(self, scores, ages):
    m = [(ages[i], scores[i]) for i in range(len(scores))]
    m = sorted(m)
    dp = [a[1] for a in m]
    for i in range(len(dp)):
        for j in range(i):
            if m[j][1] <= m[i][1] or m[j][0] == m[i][0]:
                dp[i] = max(dp[i], dp[j]+m[i][1])
    return max(dp)
