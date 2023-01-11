def majorityElement(nums):
    target = 0
    count = 0
    for num in nums:
        if count == 0:
            target = num
        elif num == target:
            count += 1
        else:
            count -= 1
    return target