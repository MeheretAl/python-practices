def dailyTemperatures(temperatures: list[int]) -> list[int]:
    ans = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            prev_index = stack.pop()
            ans[prev_index] = i - prev_index
        stack.append(i)

    return ans

nums1 = [89,62,70,58,47,47,46,76,100,70]
print(dailyTemperatures(nums1))
