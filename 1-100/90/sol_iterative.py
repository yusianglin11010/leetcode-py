def subsetsWithDup(nums):
    nums.sort()
    solution = [[]]
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            tmp = [item + [nums[i]] for item in tmp]
        else:
            tmp = []
            for current in solution:
                tmp.append(current + [nums[i]])
        solution += tmp
    return solution