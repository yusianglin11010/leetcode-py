# https://leetcode.com/problems/palindrome-number/description/
def isPalindrome(x):
    if x < 0:
        return False
    tmp = x
    val = 0
    while tmp:
        val = val * 10 + tmp % 10
        tmp //= 10
    return val == x