# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
def findCheapestPrice(n, flights, src, dst, k):
    price = [float("inf") for _ in range(n)]
    for s, d, cost in flights:
        if s == src:
            price[d] = cost
    for _ in range(k):
        current_price = [*price]
        for s, d, cost in flights:
            current_price[d] = min(current_price[d], price[s]+cost)
        price = [*current_price] 
    return price[dst] if price[dst] != float("inf") else -1