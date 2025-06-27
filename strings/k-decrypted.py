def decryt(s,k):
    decompressed_length = 0
    i = 0
    while i < len(s):
        substring = ""
        while i < len(s) and s[i].isalpha():
            substring+=s[i]
            i+=1
        freq = ""
        while i < len(s) and s[i].isdigit():
            freq+=s[i]
            i+=1
        freq = int(freq)
        if decompressed_length + (len(substring)*freq)>=k:
            index_in_expanded = k - decompressed_length -1
            return substring[index_in_expanded % len(substring)]
        decompressed_length+=len(substring)*freq
    return ""
s = 'a2b3cd3'
k = 8
print(decryt(s,k))
        