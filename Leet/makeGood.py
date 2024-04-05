def makeGood(s:str) -> str:

    '''
    Given a string s of lower and upper case English letters.
    A good string is a string which doesn't have two 
    adjacent characters s[i] and s[i + 1] where:
    1) 0 <= i <= s.length - 2
    2) s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
    '''
    #s = "leEeetcode"
    #check if the current element i.e s[i] is a bad pair with the one on top of the stack
    # if so remove it if not add it to the top of the stack and keep iterating
    size = len(s)
    stack = []
    for i in range(size):
        if stack and stack[-1] != s[i] and (stack[-1].upper == s[i].upper() or stack[-1].lower() == s[i].lower()):
            stack.pop()
        else:
            stack.append(s[i])
        


    return "".join(stack)


        
        
        
        
s = "leEeetcode"  
print(makeGood(s))
        
        
        #s[i] is a lower-case letter and s[i + 1] 
        #is the same letter but in upper-case or vice-versa.