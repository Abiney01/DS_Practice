def three_sum(arr):
    arr.sort()
    result = []
    for index , value in enumerate(arr):
        if index > 0 and value == arr[index-1]:
            continue
        left = index+1
        right = len(arr)-1
        while left < right:
            sum = value + arr[left] + arr[right]
            if sum > 0:
                right-=1
            elif sum < 0:
                left+=1
            else:
                result.append([value , arr[left], arr[right]])
                left+=1
                while arr[left] == arr[left-1] and left < right:
                    left+=1
    return result

arr = [-1,0,1,2,-1,-4]
print(three_sum(arr))