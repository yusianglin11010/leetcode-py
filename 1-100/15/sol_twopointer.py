def threeSum(nums):
    nums.sort()
    ans = []
    for left in range(len(nums)-2):
        if left > 0 and nums[left] == nums[left-1]:
            continue
        mid = left + 1
        right = len(nums) - 1
        while mid < right:
            sum_val = nums[left] + nums[mid] + nums[right]
            if sum_val > 0:
                right -= 1
            elif sum_val < 0:
                mid += 1
            else:
                ans.append([nums[left], nums[mid], nums[right]])
                while mid < right and nums[right] == nums[right-1]:
                    right -= 1
                while mid < right and nums[mid] == nums[mid+1]:
                    mid += 1
                right -= 1
                mid += 1
    return ans