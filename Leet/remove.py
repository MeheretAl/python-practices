def remove(nums: list[int],target:int) -> list[int]:
    
    k=0


    for i in range(len(nums)):
        if nums[i] != target:
            nums[k] = nums[i]
            k+=1
    print(nums)
    
    return k
nums = [3, 2, 2, 3, 4, 5, 2]


print(remove(nums,3))