class Solution:
    def checkValidString(self, s: str) -> bool:
        starCount = 0
        openCount = 0
        #the first pass forward
        for char in s:
            if char == ')':
                if openCount == 0:
                    if starCount == 0:
                        #the first element was a closing bracket or
                         #at one point there is more closing than open and stars combined
                        return False 
                    #there is a star to match the closing bracket even if there isn't any open left
                    starCount -= 1
                else:
                    #opening bracket exists
                    openCount -= 1  
            elif char == '(':
                openCount += 1
            else:
                starCount += 1
        #the second pass backwards
        #basically doing what we did with first pass but in backwards 
        closedCount = 0
        starCount = 0

        for i in range(len(s) - 1, -1,-1):
            if s[i] == '(':
                if closedCount == 0:
                    if starCount == 0:
                        return False
                    starCount -= 1
                else:
                    closedCount -= 1
            elif s[i] == ')':
                closedCount += 1
            else:
                starCount += 1

        return True