# https://leetcode.com/problems/add-to-array-form-of-integer/
def addToArrayForm(num, k):
    for i in range(len(num)-1, -1, -1):
        k, num[i] = divmod(num[i]+k, 10)
    return [int(i) for i in str(k)] + num if k else num