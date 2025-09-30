def length_of_longest_substring(str):
    char_set = set()
    max_len = 0
    left = 0
    for right in range(len(str)):
        while str[right] in char_set:
            char_set.remove(str[left])
            left+=1
        char_set.add(str[right])
        max_len = max(max_len,right-left+1)
    return max_len

str ="pwwkew"
print(length_of_longest_substring(str))