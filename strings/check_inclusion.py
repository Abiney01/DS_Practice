from collections import Counter
def check_inclusion(s1,s2):
    n = len(s1)
    m = len(s2)
    if n>m:
        return False
    s1_count = Counter(s1)
    window_count = Counter(s2[:n])
    if s1_count == window_count:
        return True
    for i in range(n,m):
        window_count[s2[i]]+=1
        window_count[s2[i-n]]-=1
        if window_count[s2[i - n]] == 0:
            del window_count[s2[i - n]]
        if window_count == s1_count:
            return True
    return False
s1 = "ab"
s2 = "eidbaooo"
print(check_inclusion(s1,s2))