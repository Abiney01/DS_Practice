
# for printing the matrix
def inplace_rotate(arr,n):
    for i in range(n-1,-1,-1):
        for j in range(n):
            print(arr[j][i],end=" ")
        print("\n")
        
arr1 = [[1,2,3],[4,5,6],[7,8,9]]
inplace_rotate(arr1,3)

# for inplace rotate anticlockwise 90
def rotate_anti(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]   #transpose code

    #reverse code
    for j in range(n):
        for i in range(n//2):
            arr[i][j],arr[n-1-i][j] = arr[n-1-i][j],arr[i][j]
    return arr
arr2 = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_anti(arr2,3))

# for inplace rotate clockwise 90
def rotate_clock(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]   #transpose code

    #reverse code
    for i in range(n):
        arr[i].reverse()
    return arr
arr3 = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_clock(arr3,3))