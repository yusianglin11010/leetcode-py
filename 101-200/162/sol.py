def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right-left) // 2
        if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
            return mid
        elif mid + 1 < len(nums) and nums[mid+1] > nums[mid]:
            left = mid + 1
        elif mid - 1 >= 0 and nums[mid-1] < nums[mid]:
            right = mid - 1
        else:
            right = mid - 1
