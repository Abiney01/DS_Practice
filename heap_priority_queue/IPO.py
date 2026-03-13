import heapq
def maxProfitCapital(k,w,profits,capital):
    maxProfit = []
    minCapital = [(c,p) for c,p in zip(capital,profits)]
    heapq.heapify(minCapital)
    for _ in range(k):
        while minCapital and minCapital[0][0] <= w:
            c,p = heapq.heappop(minCapital)
            heapq.heappush(maxProfit,-1 * p)
        if not maxProfit:
            break
        w += -1 * heapq.heappop(maxProfit)
    return w

k = 3
w = 0
profits = [1,4,2,3]
capital = [0,3,1,1]
print(maxProfitCapital(k,w,profits,capital))