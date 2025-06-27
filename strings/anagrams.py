def anagrams(s1,s2):
    a = sorted(s1)
    b = sorted(s2)
    if a==b:
        return 1
    return 0
s1 = "listen"
s2 = "silent"
print(anagrams(s1,s2))