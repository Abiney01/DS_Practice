def longest_subsequence(nums):
    if not nums:
            return 0
    longest = 0
    hash_set = set(nums)
    for num in nums :
        if num-1 not in hash_set:
            current = num
            length = 1
            while current+1 in hash_set:
                current+=1
                length+=1
            longest = max(longest,length)
    return longest
arr = [2,3,5,4,7,1]
print(longest_subsequence(arr))