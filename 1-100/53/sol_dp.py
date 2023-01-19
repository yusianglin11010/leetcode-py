def maxSubArray(nums):
    dp = [[0]*len(nums) for _ in range(2)]
    dp[0][0] = nums[0]
    dp[1][0] = nums[0]
    for i in range(1, len(nums)):
        dp[1][i] = max(dp[1][i-1]+nums[i], nums[i])
        dp[0][i] = max(dp[0][i-1], dp[1][i])
    return dp[0][-1]