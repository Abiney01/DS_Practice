def hammingWeight(n):
    res = 0
    while n :
        res += 1 if n & 1 else 0
        n >>= 1
    return res

# alternative
def hammingWeight(n):
    return bin(n).count('1')

n = 11
print(hammingWeight(n))