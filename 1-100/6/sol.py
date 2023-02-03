# https://leetcode.com/problems/zigzag-conversion/description/
def convert(s, numRows):
    if numRows == 1:
        return s
    arr = ["" for i in range(numRows)]
    index = 0
    step = 1
    for w in s:
        arr[index] += w
        if index == numRows-1:
            step = -1
        elif index == 0:
            step = 1
        index += step
    return "".join(arr)