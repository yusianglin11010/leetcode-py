# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
from collections import defaultdict
def minimumRounds(self, tasks):
    count = defaultdict(int)
    ans = 0
    for task in tasks:
        count[task] += 1
    for task, c in count.items():
        if c == 1:
            return -1
        else:
            ans += math.ceil(count[task] / 3)
    return ans
