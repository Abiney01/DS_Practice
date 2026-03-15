def lastWordLen(s):
    ans = s.split()
    res = ans[len(ans)-1]
    return len(res)

s = "   fly me   to   the moon  "
print(lastWordLen(s))