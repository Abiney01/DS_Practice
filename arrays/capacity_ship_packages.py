def capacity_ship_packages(nums,d):
    min_cap = max(nums)
    max_cap = sum(nums)
    while min_cap < max_cap:
        mid = (min_cap + max_cap)//2
        days = 1
        total = 0
        for i in nums:
            if total+i > mid:
                days+=1
                total = 0
            total+=i
        if days > d:
            min_cap = mid+1
        else:
            max_cap = mid
    return min_cap
nums = [2,4,6,1,3,10]
d = 4
print(capacity_ship_packages(nums,d))