def removeParentheses(s:str) -> str:
    ans = ""
    stack = []
    openCount = 0
    for i in range(len(s)):
        if s[i] == '(':
            openCount +=1
            stack.append(s[i])
        elif s[i] == ')':
            openCount -= 1
            stack.append(s[i])
        if openCount == 0:
            del stack[0]
            del stack[len(stack) - 1]
            ans += ''.join(stack)
            stack = []
    
    return ans
s = "(()())(())"
print(removeParentheses(s))