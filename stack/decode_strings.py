def decode_string(s):
    str_stack = []
    num_stack = []
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)

        elif ch == '[':
            num_stack.append(num)
            num = 0
            str_stack.append(ch)

        elif ch == ']':
            res = ""
            while str_stack[-1] != '[':
                res = str_stack.pop() + res
            str_stack.pop() 
            repeat = num_stack.pop()
            str_stack.append(res * repeat)
        else:
            str_stack.append(ch)
    return "".join(str_stack)

    
s = "2[a3[b]]c"
# s = "10[a]"
print(decode_string(s))