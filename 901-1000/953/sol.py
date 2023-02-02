# https://leetcode.com/problems/verifying-an-alien-dictionary/description/
def isAlienSorted(words, order):
    order_map = {w:idx for idx, w in enumerate(order)}
    # return if s2 > s1
    def isAlienGreater(s1, s2):
        p = 0
        while p < len(s1) and p < len(s2):
            w1, w2 = s1[p], s2[p]
            if order_map[w2] > order_map[w1]:
                return True
            elif order_map[w2] == order_map[w1]:
                p += 1
            elif order_map[w2] < order_map[w1]:
                return False
        # note that the empty blank should be considered greater than any character
        return len(s2) >= len(s1)
    for i in range(len(words)-1):
        if not isAlienGreater(words[i], words[i+1]):
            return False
    return True