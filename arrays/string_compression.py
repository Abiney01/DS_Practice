def string_compression(string):
    n = len(string)
    i = 0
    idx = 0
    while i < n:
        count = 0
        char = string[i]
        while i < n and char == string[i]:
            count+=1
            i+=1
        if count == 1:
            string[idx] = char
            idx+=1
        else:
            string[idx] = char
            idx+=1
            count_str = str(count)
            for char_count in count_str:
                string[idx] = char_count
                idx+=1

    return idx

string = ["a","a","b","b","c","c","c"]
print(string_compression(string))