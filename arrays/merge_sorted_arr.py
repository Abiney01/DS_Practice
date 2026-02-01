def merge_sorted_arr(num1,num2,m,n):
    last = m + n - 1
    i = m - 1
    j = n - 1
    while j >= 0:
        if i >=0 and num1[i] > num2[j]:
            num1[last] = num1[i]
            i-=1
        else:
            num1[last] = num2[j]
            j-=1
        last-=1
    return num1
num1 = [10,20,30,40,0,0]
num2 = [1,2]
n = 4
m = 2
print(merge_sorted_arr(num1,num2,n,m))
        
