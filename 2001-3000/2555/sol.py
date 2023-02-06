# https://leetcode.com/problems/maximize-win-from-two-segments/description/
    def maximizeWin(self, p: List[int], k: int) -> int:
        dp = [0 for _ in range(len(p)+1)]
        res = j = 0
        for i, a in enumerate(p):
            # to make sure our interval is fulfill the segment
            while p[i]-k > p[j]: j+=1
            # we need to decide if the current segment is greater than the previous segments
            dp[i+1] = max(dp[i], i-j+1)
            # the result would be the current segment + previous maximum segment
            res = max(res, dp[j]+i-j+1)
        return res
