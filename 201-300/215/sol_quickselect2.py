def findKthLargest(nums, k):
    def findKthSmallest(nums, k):
        pos = partition(nums, 0, len(nums)-1)
        if pos + 1 > k: 
            return findKthSmallest(nums[:pos], k) # because nums[:pos] in fact contain pos+1 elements
        elif pos + 1 < k:
            return findKthSmallest(nums[pos+1:], k - pos - 1) 
            # because nums[:pos] exactly contains pos+1 elements 
            # all nums[:pos], that is for all that pos+1 elements are not we want
        else:
            return nums[pos]
    def partition(nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
    return findKthSmallest(nums, len(nums) - k + 1)