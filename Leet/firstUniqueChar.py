def firstUniqChar(s: str) -> int:
    freq = {}
    indexHold = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            indexHold[char] = s.index(char)


    for char in freq:
        if freq[char] == 1:
            return indexHold[char]

    return -1


s = "leetcode"
print(firstUniqChar(s))
