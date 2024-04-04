def maxDepth(s:str) -> int:
    answer,openCount = 0,0
    for char in s:
        if char == '(':
            openCount +=1
        elif char == ')':
            openCount -= 1
        answer = max(answer,openCount)

    return answer


