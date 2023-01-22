def isPalindrome(w):
    left, right = 0, len(w) - 1
    while right > left:
        if w[left] != w[right]:
            return False
        left += 1
        right -= 1
    return True
def partition(s):
    ans = []
    def backtrack(s, tmp):
        if not s:
            ans.append(tmp.copy())
            return 
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                backtrack(s[i:], tmp + [s[:i]])
    backtrack(s, [])
    return ans