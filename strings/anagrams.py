def anagrams(s1,s2):
    # a = sorted(s1)
    # b = sorted(s2)
    # if a==b:
    #     return 1
    # return 0

    # optimal O(n) O(1) -> time and space 
    if len(s1)!=len(s2):
         return False
    count = [0]*26
    for i in range(len(s1)):
        count[ord(s1[i]) - ord('a')]+=1
        count[ord(s2[i]) - ord('a')]-=1
    for val in count:
        if val!=0:
            return False
        return True
s1 = "listen"
s2 = "silent"
print(anagrams(s1,s2))