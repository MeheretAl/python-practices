def monotonicIncreasing(nums:list[int]) -> list[int]:
    stack = []
    result = []

    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()

        stack.append(num)
    
    while stack:
        result.insert(0,stack.pop())

    return result

check = [1,5,2,3,4,7,4,6]
print(monotonicIncreasing(check))