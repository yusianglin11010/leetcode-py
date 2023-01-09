def canCompleteCircuit(gas, cost):
    n = len(gas)
    diff = []
    for i in range(n):
        diff.append(gas[i] - cost[i])
    if sum(diff) < 0:
        return -1
    tank, start = 0, 0
    for i in range(n):
        tank += diff[i]
        if tank < 0:
            tank = 0
            start = i+1
    if start == n:
        return 0
    return start