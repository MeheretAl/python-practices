from collections import Counter

def customSortString(order: str, s: str) -> str:
    charCounter = Counter(s)
    ans = ""
    for char in order:
        if char in charCounter:
            ans += char * charCounter[char]
            charCounter[char]=0
        
    for char,count in charCounter.items():
        ans += char * count
        
    return ans
    
order = "cba"
s = "csadd"
answer = customSortString(order,s)
print(answer)
