def assign_cookies(g,s):
    g.sort()
    s.sort()
    i = 0
    j = 0
    res = 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            res+=1
            i+=1
        j+=1
    return res

g=[10,9,8,7]
s=[5,6,7,8]
print(assign_cookies(g,s))
