def maxSatisfied(customers,grumpy,minutes):
    l = 0
    window = 0
    max_window = 0
    satisfied = 0
    for r in range(len(customers)):
        if grumpy[r]:
            window += customers[r]
        else:
            satisfied += customers[r]
        if r-l+1 > minutes:
            if grumpy[l]:
                window -= customers[l]
            l+=1
        max_window = max(max_window,window)
    return satisfied + max_window

customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
print(maxSatisfied(customers,grumpy,minutes))