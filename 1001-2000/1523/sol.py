# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
def countOdds(low, high):
    if low%2:
        return (high-low)//2+1
    return (high-low+1) // 2