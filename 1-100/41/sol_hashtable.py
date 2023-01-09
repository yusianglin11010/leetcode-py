# O(1) time but O(n) space
def firstMissingPositive(self, nums: List[int]) -> int:
    s = set(nums)
    i = 1
    while i:
        if i not in s:
            return i
        i += 1