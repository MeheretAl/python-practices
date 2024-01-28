
def shortestToChar(word: str, c: str) -> list[int]:
    
    answer = []

    for i in range(len(word)):
        minimum = 10000000
        for j in range(len(word)):
            if c == word[j]:
                distance = abs(i-j)
                minimum = min(distance,minimum)
        answer.append(minimum)
    return answer




            
s = "loveleetcode"
c = "e"
print(shortestToChar(s,c))