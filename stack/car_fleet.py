def car_fleet(pos,speed,target):
    pair = [(p,s) for p,s in zip(pos,speed)]
    pair.sort(reverse=True)
    stack = []
    for p , s in pair:
        stack.append((target-p)/s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

target = 10
pos = [4,1,0,7] 
speed = [2,2,1,1]
print(car_fleet(pos,speed,target))
