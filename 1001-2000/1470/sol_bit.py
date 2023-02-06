# https://leetcode.com/problems/shuffle-the-array/ 
# O(n), O(1)
def shuffle(nums, n):
    ans = []
    for i in range(n):
        nums[i] = nums[i] << 10
        nums[i] = nums[i] | nums[i+n]
    
    j = 2 * n - 1
    for i in range(n-1, -1, -1):
        # 2**10 is 1000000000, so 2**10 -1 would be 111111111
        y = nums[i] & (2**10 - 1)
        x = nums[i] >> 10
        nums[j] = y
        nums[j-1] = x
        j -= 2
    return nums