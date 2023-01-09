def canCompleteCircuit(gas, cost):
    n = len(gas)
    for start in range(n):
        tank = 0
        for step in range(n):
            i = (start + step) % n
            tank += gas[i]
            tank -= cost[i]
            if tank < 0:
                break
        if tank >= 0:
            return start
    return -1