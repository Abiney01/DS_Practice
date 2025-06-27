def first_non_repeating(str):
    # for i in range(len(str)):
    #     c = 0
    #     c = str.count(str[i])
    #     if c==1:
    #         return str[i]
    # return str[0]

    # approach 2
    char_count = {}
    for i in str:
        print(i)
        char_count[i] = char_count.get(i,0)+1
    for j in str:
        if char_count[j]==1:
            return j
    return str[0]
str = 'aabbccd'
print(first_non_repeating(str))