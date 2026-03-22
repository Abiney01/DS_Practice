def avg_waiting_time(customers):
    total = 0
    t = 0
    for arrival,order in customers:
        total += max(t - arrival,0)
        t = max(t,arrival)
        total += order
        t += order
    return total/len(customers)

customers = [[1,2],[2,5],[4,3]]
print(avg_waiting_time(customers))