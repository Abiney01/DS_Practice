def adding_spaces_string(string,spaces):
    i,j = 0,0
    res = []
    while i < len(string) and j < len(spaces):
        if i < spaces[j]:
            res.append(string[i])
            i+=1
        else:
            res.append(" ")
            j+=1
    if i < len(string):
        res.append(string[i:])
    return "".join(res)
string = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
print(adding_spaces_string(string,spaces))