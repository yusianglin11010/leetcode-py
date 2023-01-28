class SummaryRanges:

    def __init__(self):
        self.s = set()
        self.heap = []
        
    def addNum(self, value: int) -> None:
        if value not in self.s:
            self.s.add(value)
            heapq.heappush(self.heap, [value, value])
    
    def getIntervals(self) -> List[List[int]]:
        tmp = []
        while self.heap:
            cur = heapq.heappop(self.heap)
            if tmp and cur[0] <= tmp[-1][1] +1:
                tmp[-1][1] = max(cur[1], tmp[-1][1])
            else:
                tmp.append(cur)
        self.heap = tmp
        return self.heap