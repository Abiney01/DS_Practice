def longest_repeating_char(str,k):
    count = {}
    left = 0
    max_f = 0
    res = 0
    for right in range(len(str)):
        count[str[right]] = 1 + count.get(str[right],0)
        max_f = max(max_f,count[str[right]])
        while (right-left+1) - max_f > k:
            count[str[left]]-=1
            left+=1
        res = max(res,right-left+1)
    return res

str = "AAABABB"
k = 1
print(longest_repeating_char(str,k))
