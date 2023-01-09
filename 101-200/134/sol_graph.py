def canCompleteCircuit(gas, cost):
    sum_val, min_sum, start = 0, 0, 0
    for i in range(len(gas)):
        sum_val += gas[i] - cost[i]
        if sum_val < min_sum:
            start = i + 1
            min_sum = sum_val
    if sum_val < 0:
        return -1
    if start == len(gas):
        return 0
    return start