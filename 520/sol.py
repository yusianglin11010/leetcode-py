# https://leetcode.com/problems/detect-capital/description/
def detectCapitalUse(self, word):
    cap_number = 0
    for w in word:
        cap_number += w.isupper()
    return cap_number == len(word) or cap_number == 0 or (cap_number == 1 and word[0].isupper())

                
