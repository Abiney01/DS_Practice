import sys 
def next_palindrome(s):
#    num = int(s)
#    for i in range(num+1,sys.maxsize):
#         if str(i) == str(i)[::-1]:
#             return i
    n = len(s)
    if s == '9'*n:
        return '1'+ '0'*(n-1)+'1'
    left_half = s[:(n+1)//2]
    if n%2==0:
        candidate = left_half + left_half[::-1]
    else:
        candidate = left_half + left_half[-2::-1]
    if candidate > s :
        return candidate
    left_half = str(int(left_half)+1)
    if n%2==0:
        new_palindrome = left_half + left_half[::-1]
    else:
        new_palindrome = left_half + left_half[-2::-1]
    return new_palindrome


s = "1441"
print(next_palindrome(s))