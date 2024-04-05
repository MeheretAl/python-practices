def reverseString(s:list[str]) -> str:
    leftptr,rightptr = 0,len(s) - 1
    while leftptr < rightptr:
        s[leftptr],s[rightptr] = s[rightptr],s[leftptr]
        leftptr+=1
        rightptr-=1
    
    return s

s = ["h","e","l","l","o"]
print(reverseString(s))