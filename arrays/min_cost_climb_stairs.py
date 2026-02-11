def min_cost_stairs(cost):
    min_cost = [0] * (len(cost)+1)
    for i in range(2,len(cost)+1):
        min_cost[i] = min((cost[i-1]+min_cost[i-1]),(cost[i-2]+min_cost[i-2]))
    return min_cost[i]

cost = [1,2,1,2,1,1,1]
print(min_cost_stairs(cost))