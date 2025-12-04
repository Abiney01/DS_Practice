def check_permutations(str1,str2):
    return sorted(str1) == sorted(str2)

str1 = "abc"
str2 = "bca"
print(check_permutations(str1,str2))