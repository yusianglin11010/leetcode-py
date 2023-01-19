def maxSubarraySumCircular(nums):
    max_val, cur_max, min_val, cur_min = -float.inf, -float.inf, float.inf, float.inf
    for num in nums:
        cur_max = max(num, cur_max + num)
        max_val = max(max_val, cur_max)
        cur_min = min(num, cur_min + num)
        min_val = min(min_val, cur_min)
    ans = max(max_val, sum(nums)-min_val)
    if max_val > 0:
        return ans
    return max_val
