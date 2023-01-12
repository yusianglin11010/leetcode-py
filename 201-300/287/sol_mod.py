def findDuplicate(nums):
    n = len(nums)
    for num in nums:
        nums[num%n] += n
    for idx, num in enumerate(nums):
        if num // n > 1:
            return idx
