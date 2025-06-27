def minimum_parantheses(s):
    result = 0
    open_count = 0
    for i in s:
        if i=='(':
            open_count+=1
        else:
            if open_count > 0:
                open_count-=1
            else:
                result+=1
    return result + open_count
s = ")((())"
print(minimum_parantheses(s))