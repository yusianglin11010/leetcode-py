def subsets(nums):
    solution = [[]]
    for element in nums:
        tmp = []
        for current in solution:
            tmp.append(current + [element])
        solution += tmp
    return solution