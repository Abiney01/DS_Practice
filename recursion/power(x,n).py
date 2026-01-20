def pow(x,n):
    def helper(x,n):
        if x == 0:
            return 0 
        if n == 0:
            return 1
        result = helper(x,n//2)
        result = result * result
        return  x * result if n%2 else result
    res = helper(x,abs(n))
    return res if n >=0 else 1/res

print(pow(2,5))