import math
# def sqrt_number(n):
#     return math.floor(n**0.5)
# n = int(input())
# print(sqrt_number(n))

def mySqrt(x):
        l = 1
        r = x
        res = 0
        while l <= r:
            mid = (l + r)//2
            if math.floor(mid*mid) == x:
                return mid
            elif math.floor(mid*mid) < x:
                l = mid + 1
                res = mid
            else:
                r = mid - 1
        return res
print(mySqrt(13))