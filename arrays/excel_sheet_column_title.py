def column_title(columnNumber):
    res = ""
    while columnNumber > 0:
        offset = (columnNumber-1) % 26
        res += chr(ord("A") + offset)
        columnNumber = (columnNumber-1)//26
    return res[::-1]

print(column_title(34))