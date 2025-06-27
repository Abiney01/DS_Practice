def reverse_word(string):
    a = string.split(" ")
    a.reverse()
    return " ".join(a).strip() #used for removing extra spaces
string = "Hello this is NodeJs"
print(reverse_word(string))