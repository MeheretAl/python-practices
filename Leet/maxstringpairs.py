def maximumNumberOfStringPairs(words: list[str]) -> int:
    answer = 0
    for i in range(len(words)):
        curr = words[i]
        for j in range(i + 1, len(words)):
            reversedWord = "".join(reversed(words[j]))
            if curr == reversedWord:
                answer += 1

    return answer


words = ["cd", "ac", "dc", "ca", "zz"]
print(maximumNumberOfStringPairs(words))
