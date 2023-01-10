def findKthLargest(nums, k):
    left, mid, right = [], [], []
    pivot = nums[0]
    left = [x for x in nums if x > pivot]
    right = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    L, M = len(left), len(mid)
    if L >= k:
        return findKthLargest(left, k)
    elif k > L+M:
        return findKthLargest(right, k-L-M)
    else:
        return mid[0]
