# https://leetcode.com/problems/find-the-town-judge/description/
def findJudge(n, trust):
    d = defaultdict(set)
    for a, b in trust:
        d[a].add(b)
    judge = 0
    for i in range(1,n+1):
        if not d[i]:
            judge = i
    for k,v in d.items():
        if k != judge and judge not in v:
            return -1
    return judge