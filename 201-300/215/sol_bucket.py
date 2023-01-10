def findKthLargest(nums, k):
    min_val, max_val = min(nums), max(nums)
    bucket = [0 for _ in range(min_val, max_val+1)]
    for num in nums:
        bucket[num-min_val] += 1
    i = max_val - min_val
    while True:
        k -= bucket[i]
        if k <= 0:
            return i + min_val
        i -= 1