def binaryStringWithNoConsecutive1s(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    return binaryStringWithNoConsecutive1s(n-1) + binaryStringWithNoConsecutive1s(n-2)
print(binaryStringWithNoConsecutive1s(4))