# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
def singleNonDuplicate(nums):
    l, r = 0, len(nums) - 1
    while r >= l:
        mid = l + (r-l)//2
        if (mid == len(nums)-1 or nums[mid+1] != nums[mid]) and (mid == 0 or nums[mid-1] != nums[mid]):
            return nums[mid]
        else:
            leftSize = mid - 1 if nums[mid-1] == nums[mid] else mid
            if leftSize %2 == 1:
                r = mid - 1
            else:
                l = mid + 1
    