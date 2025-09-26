from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)

    for word in words:
        # Sort the word and use it as a key
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())
    # for sorting in the same order as the input
    # result = []
    # for i in anagram_map.values():
    #     i.sort()
    #     result.extend(i)
    # return ' '.join(result)

# Example usage
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(result)
