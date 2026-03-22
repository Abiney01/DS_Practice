from collections import Counter
def custom_sort_string(order,s):
    counter = Counter(s)
    res = []

    for char in order:
        if char in counter:
            res.extend([char] * counter[char])
            del counter[char]

    for char,count in counter.items():
        res.extend([char]*count)
        
    return "".join(res)

order = "bfg"
s = "agbfcdb"
print(custom_sort_string(order,s))