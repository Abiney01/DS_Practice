def longest_common_prefix(strs):
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return s[:i]
    return strs[0]

nums = ["dance","dag","danger","damage"]
print(longest_common_prefix(nums))