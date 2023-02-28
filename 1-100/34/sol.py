# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
def searchRange(nums, target):
    def binary_search_left(nums, target):
        l, r = 0, len(nums) - 1
        while r >= l:
            mid = l + (r-l)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                r = mid - 1
        if l == len(nums) or nums[l] != target: return -1
        else: return l
    def binary_search_right(nums, target):
        l, r = 0, len(nums) - 1
        while r >= l:
            mid = l + (r-l)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        if r < 0 or nums[r] != target: return -1
        else: return r
    return [binary_search_left(nums, target), binary_search_right(nums, target)]