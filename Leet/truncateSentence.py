def truncateSentence(s: str, k: int) -> str:
    wordList = []
    wordList = (s.split(" "))
    answer = ""
    for i in range(k):
        if i < k - 1:
            answer += wordList[i] + " "
        else:
            answer += wordList[i]
    return answer

s = ("Hello how are you Contestant")
k = 4

print(truncateSentence(s, k))