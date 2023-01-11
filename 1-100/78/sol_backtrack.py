def subsets(nums):
    ans = [[]]
    tmp = []
    def backtrack(nums):
        for i in range(len(nums)):
            tmp.append(nums[i])
            ans.append(tmp.copy())
            backtrack(nums[i+1:])
            tmp.pop()
    backtrack(nums)
    return ans