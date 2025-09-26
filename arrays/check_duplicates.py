def check_duplicate(arr):
    for i in arr:
        if arr.count(i) > 0 :
            return True
    return False

arr = [1,2,3,4]
print(check_duplicate(arr))
