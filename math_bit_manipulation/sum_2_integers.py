def getSum(a,b):
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b!=0:
            carry = (a&b) & mask
            a = (a^b) & mask
            b = (carry << 1) & mask
        return a if a <= max_int else ~(a^mask)

print(getSum(3,4))