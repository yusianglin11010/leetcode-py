# https://leetcode.com/problems/put-marbles-in-bags/description/
from heapq import nlargest, nsmallest
def putMarbles(weights k):
    arr = [weights[i] + weights[i+1] for i in range(len(weights)-1)]
    return sum(nlargest(k-1, arr)) - sum(nsmallest(k-1, arr))