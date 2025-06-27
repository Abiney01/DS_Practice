def rotate(arr):
    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])
    return arr
# n = int(input())
arr = list(map(int,input().split()))
k = int(input())
print(rotate(arr))


