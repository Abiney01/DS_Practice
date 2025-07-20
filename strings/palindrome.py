import re 
def check_palindrome(num):
    if len(num) == 1:
        a = num[0]
        if num == a[::-1]:
            print("Yes")
        else:
            print("No")
    else:
        a = num[::-1]
        if a == num:
            print("Yes")
        else:
            print("No")

num = input().split(" ")
check_palindrome(num)

def palindrome(str):
    str = str.lower()
    cleaned = re.sub(r'[^a-z0-9]', '', str)
    return cleaned == cleaned[::-1]
str = input()
print(palindrome(str))