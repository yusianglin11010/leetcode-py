# https://leetcode.com/problems/search-insert-position/
def searchInsert(nums, target):
    l, r = 0, len(nums)-1
    while r >= l:
        mid = l + (r-l) // 2
        if target > nums[mid]:
            l = mid + 1
        elif target > nums[mid]:
            r = mid - 1
        else:
            r = mid - 1
    return l
