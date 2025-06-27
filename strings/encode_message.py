def run_length_encoding(s):
    encoded_string = ""
    count = 1
    for i in range(1,len(s)+1):
        if i<len(s) and s[i]==s[i-1]:
            count+=1
        else:
            encoded_string+=s[i-1]+str(count)
            count = 1
    return encoded_string

s = "aabbcdde"
print(run_length_encoding(s))
