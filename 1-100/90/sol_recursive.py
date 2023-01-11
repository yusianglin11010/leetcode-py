def subsetsWithDup(nums):
    ans = []
    nums.sort()
    def dfs(nums, path):
        ans.append(path.copy())
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            dfs(nums[i+1:], path+[nums[i]])
    dfs(nums, [])
    return ans
