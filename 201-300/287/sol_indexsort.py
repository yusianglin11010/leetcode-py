def findDuplicate(nums):
    i = 0
    while i < len(nums):
        n = nums[i]
        if n == i+1:
            i += 1
        elif n == nums[n-1]:
            return nums[i]
        else:
            nums[i] = nums[n-1]
            nums[n-1] = n