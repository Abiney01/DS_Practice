def numRescueBoats(people,limit):
    people.sort()
    left = 0
    right = len(people)-1
    res = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left+=1
        right-=1
        res+=1
    return res

people = [3,5,3,4]
limit = 6
print(numRescueBoats(people,limit))