def simplify_path(path):
    stack = []
    curr = ""
    for c in path + "/":
        if c == "/":
            if curr == "..":
                if stack : stack.pop()
            elif curr != "" and curr !=".":
                stack.append(curr)
            curr = ""
        else:
            curr+=c
    return "/"+"/".join(stack)

path = "/neetcode/practice//...///../courses"
print(simplify_path(path))