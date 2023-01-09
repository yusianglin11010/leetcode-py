from collections import Counter

def maxPoints(self, points) -> int:
    def get_slope(p1, p2):
        if p1[0]-p2[0] == 0:
            return inf
        return (p1[1]-p2[1]) / (p1[0]-p2[0])
    ans = 0
    for i in range(len(points)):
        c = Counter()
        for j in range(i+1,len(points)):
            slope = get_slope(points[i], points[j])
            c[slope] += 1
            ans = max(c[slope], ans)
    return ans + 1