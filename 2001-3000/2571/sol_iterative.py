# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/
def minOperations(n):
    candi = [pow(2,i) for i in range(17)]
    ans = 0
    while n:
        min_dif = inf
        close_pow = None
        for i in candi:
            if abs(n-i) < min_dif:
                min_dif = abs(n-i)
                close_pow = i
        n = abs(close_pow - n)
        ans += 1
    return ans