def word_breakII(s,wordDict):
    set_word = set(wordDict)
    res = []
    curr = []
    def backtrack(i):
        if i == len(s):
            res.append(" ".join(curr))
            return
        for j in range(i,len(s)):
            w = s[i:j+1]
            if w in set_word:
                curr.append(w)
                backtrack(j+1)
                curr.pop()

    backtrack(0)
    return res

s = "racecariscar"
wordDict = ["racecar","race","car","is"]
print(word_breakII(s,wordDict))