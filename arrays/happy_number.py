def happy_number(n):
    used_numbers = set()
    while True:
        result = 0  
        while n!=0:
            result+=(n%10) ** 2
            n = n//10
        if result == 1:
            return True
        n = result
        if n in used_numbers:
            return False
        used_numbers.add(n)
    
print(happy_number(22))