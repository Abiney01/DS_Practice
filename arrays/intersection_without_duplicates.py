def intersection(arr,brr):
    set_arr = set(arr)
    result = []
    for i in brr:
        if i in set_arr:
            result.append(i)
            set_arr.remove(i)
    return result



arr = [1,2,2,1]
brr = [2,2]
print(intersection(arr,brr))