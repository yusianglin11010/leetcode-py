# https://leetcode.com/problems/delete-columns-to-make-sorted/
def minDeletionSize(self, strs):
    n = len(strs)
    ans = 0
    for i in range(len(strs[0])):
        row = 0
        while row < n-1:
            if ord(strs[row][i]) > ord(strs[row+1][i]):
                ans += 1
                break
            row += 1
    return ans