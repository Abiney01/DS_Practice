def gcd_strings(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    def isCommonDivisor(l):
        if l1 % l or l2 % l:
            return False
        f1 = l1 // l
        f2 = l2 // l
        return str1[:l] * f1 == str1 and str1[:l] * f2 == str2  
    for l in range(min(l1,l2),0,-1):
        if isCommonDivisor(l):
            return str1[:l]
    return ""

str1 = "NANANA"
str2 = "NANA"
print(gcd_strings(str1,str2))