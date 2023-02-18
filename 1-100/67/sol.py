# https://leetcode.com/problems/add-binary/
def addBinary(a, b):
    a, b = a[::-1], b[::-1]
    carry = 0
    ans = ""
    for i in range(max(len(a), len(b))):
        a_i = 0 if i >= len(a) else int(a[i])
        b_i = 0 if i >= len(b) else int(b[i])
        val = carry + a_i + b_i
        carry = val >= 2
        ans = str(val%2) + ans
    if int(carry):
        ans = "1" + ans
    return ans 
