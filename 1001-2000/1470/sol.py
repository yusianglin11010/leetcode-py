# https://leetcode.com/problems/shuffle-the-array/
# O(1), O(1)
def shuffle(nums, n):
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
    return ans