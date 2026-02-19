from collections import deque
def dota2Senate(senators):
    R , D = deque() , deque()
    for i,val in enumerate(senators):
        if val == "R":
            R.append(i)
        else:
            D.append(i)
    
    while R and D:
        rTurn = R.popleft()
        dTurn = D.popleft()

        if rTurn < dTurn:
            R.append(rTurn+len(senators))
        else:
            D.append(dTurn+len(senators))
    return "Radiant" if R else "Dire"

senators = "RRDDD"
print(dota2Senate(senators))