class SummaryRanges:

    def __init__(self):
        self.s = set()
        
    def addNum(self, value: int) -> None:
        self.s.add(value)
    
    def getIntervals(self) -> List[List[int]]:
        prev = -1
        intervals = []
        for num in sorted(self.s):
            if prev == -1:
                intervals.append([num,num])
            elif num - prev == 1:
                intervals[-1][1] = num
            else:
                intervals.append([num, num])
            prev = num
        return intervals