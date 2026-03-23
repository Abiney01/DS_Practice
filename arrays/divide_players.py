def divide_players(skill):
    n = len(skill)
    if n % 2:
        return -1
    skill.sort()
    i = 0
    j = n - 1
    total = 0
    target = skill[0] + skill[-1]
    while i < j:
        if skill[i] + skill[j] != target:
            return - 1
        total += skill[i] + skill[j]
        i+=1
        j-=1
    return total
    
skill = [2,4,1,3]
print(divide_players(skill))