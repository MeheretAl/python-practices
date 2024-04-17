def frequencySort(s: str) -> str:
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    answer = ""
    sortedItems = sorted(freq.items(),  key=lambda x:x[1],reverse=True)
    print(sortedItems)
    for item in sortedItems:
        answer += item[0] * item[1]
    print(answer)

s = "ccccaaaaddddddd"
print(frequencySort(s))