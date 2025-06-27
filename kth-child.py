def kth_child(n,k):
    parent = 'M'
    while n > 1:
        if k%2 == 0:
            if parent == "M":
                parent = "F"
            else:
                parent = "M"
        else:
            parent = parent
        k = (k+1)//2
        n-=1
    return "Male" if parent == "M" else "Female"
n = 4
k = 3
print(kth_child(n,k))

# Generation 1:   1 → [M]
# Generation 2:   1   2 → [M  F]
# Generation 3:   1   2   3   4 → [M  F  F  M]
# Generation 4:   1   2   3   4   5   6   7   8 → [M  F  F  M  F  M  M  F]
