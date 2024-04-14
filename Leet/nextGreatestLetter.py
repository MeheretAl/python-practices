def nextGreatestLetter(letters: list[str], target: str) -> str:
    left = 0
    right = len(letters) - 1
    
    ans = letters[0] 
    
    if letters[0] > target or letters[right] < target:
        return ans
    
        
    while left <= right:
        mid = (left + right) // 2
        
        if letters[mid] <= target:
            left = mid + 1
        else:
            ans = letters[mid]
            right = mid - 1
            
    return ans
