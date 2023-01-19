def maxSubArray(nums):
    prev = 0
    ans = -float.inf
    for i in range(len(nums)):
        if prev > 0:
            nums[i] += prev
        prev = nums[i]
        ans = max(ans, nums[i])
    return ans