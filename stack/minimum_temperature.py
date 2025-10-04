def minimum_temperature(temp):
    res = [0]*len(temp)
    stack = []
    for i,t in enumerate(temp):
        while stack and t> stack[-1][0]:
            stackT,stackInd = stack.pop()
            res[stackInd] = (i-stackInd)
        stack.append([t,i])
    return res

temperatures = [30,38,30,36,35,40,28]
print(minimum_temperature(temperatures))