def minRemoveToMakeValid(s: str) -> str:
        stack = []
        openCount = 0
        #for the first pass
        for i in range(len(s)):
            if s[i] == '(':
                openCount += 1
                stack.append(s[i])
            elif s[i] == ')':
                openCount -= 1
                if openCount >= 0:
                    stack.append(s[i])
                else:
                    openCount = 0
            else:
                stack.append(s[i])
       
        #for the second pass 
        #from the back to the front
        closeCount = 0
        for i in range(len(stack) - 1,-1,-1):
            if stack[i] == ')':
                closeCount += 1
            elif stack[i] == '(':
                closeCount -= 1
                if closeCount < 0:
                    closeCount = 0
                    del stack[i]
            
        return "".join(stack)