def beautiful_string(s):
    n = len(s)
    count1 = sum(1 for i in range(n) if s[i]!=('0' if i%2==0 else '1'))
    count2 = sum(1 for i in range(n) if s[i]!=('1' if i%2==0 else '0'))
    return min(count1,count2)
    
print(beautiful_string("0000"))