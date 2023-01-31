# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/description/
# (0,0) -> (0,0)
# (1,0) -> (1,1), (1|0)(1^0) = 11
# (0,1) -> (1,1), (1|0)(1^0) = 11
# (1,1) -> (1,0)
def makeStringsEqual(s, target):
    return ("1" in s) == ("1" in target)