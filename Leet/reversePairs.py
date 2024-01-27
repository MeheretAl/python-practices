def reversePairs(nums: list[int]) -> int:
    counter = 0
    half = len(nums) // 2
    first = [nums[i] for i in range(half)]
    second = [nums[i] for i in range(half, len(nums))]
    
    for i in range(half):
        j = 0
        while j < len(second):
            if first[i] > 2 * second[j]:
                counter += 1
            j += 1

    return counter


nums = [1,3,2,3,1]
answer = reversePairs(nums=nums)
print(answer)
