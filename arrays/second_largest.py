def second_largest(arr):
    if len(arr)<2:
        return - 1
    first_largest,second_largest = float('-inf'),float('-inf')
    for num in arr:
        if num>first_largest:
            second_largest = first_largest
            first_largest = num
        elif first_largest>num>second_largest:
            second_largest = num
    return second_largest if second_largest!=float('-inf') else -1

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    print(second_largest(arr))