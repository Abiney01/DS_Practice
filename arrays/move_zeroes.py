def move_zeroes(arr):
    insert_position = 0
    for i in arr:
        if i!=0:
            arr[insert_position] = i
            insert_position+=1
    while insert_position<len(arr):
        arr[insert_position] = 0
        insert_position+=1
    return arr
arr = [0,1,0,3,12]
print(move_zeroes(arr))