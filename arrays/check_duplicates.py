def check_duplicate(arr):
    # for i in arr:
    #     if arr.count(i) > 0 :
    #         return True
    # return False

    # optimal O(n) and O(n) -> Time and Space
    hashset = set()
    for i in arr:
        if i in hashset:
            return True
        hashset.add(i)
    return False


arr = [1,2,3,4]
print(check_duplicate(arr))
