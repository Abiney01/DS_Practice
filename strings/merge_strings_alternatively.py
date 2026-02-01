def merge_str_alternatively(word1,word2):
    i = 0
    j = 0
    res = ""
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            res+=word1[i]
            i+=1
        if j < len(word2):
            res+=word2[j]
            j+=1
    return res

word1 = "hello"
word2 = "zero"
print(merge_str_alternatively(word1,word2))