def insert(intervals, newInterval):
    res = []
    for idx, interval in enumerate(intervals):
        if interval[1] < newInterval[0]:
            res.append(interval)
        elif newInterval[1] < interval[0]:
            res.append(newInterval)
            return res + intervals[idx:]
        else:
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])
    res.append(newInterval)
    return res