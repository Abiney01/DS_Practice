def minimumLengthEncoding(words):
    words = set(words)  
    for w in list(words):
        for i in range(1, len(w)):
            suffix = w[i:]
            if suffix in words:
                words.remove(suffix)
    return sum(len(w) + 1 for w in words)

words = ["time", "me", "bell"] 
print(minimumLengthEncoding(words))