def applyOperations(nums:list[int]) -> list[int]:
    size = len(nums)
    for i in range(size-1):
        if nums[i] == nums[i+1]:
            nums[i]*=2
            nums[i+1] = 0
    i = 0
    for j in range(size):
        if nums[j] != 0:
            nums[j],nums[i] = nums[i],nums[j]
            i+=1
    
    return nums


nums = [0,1]
print(applyOperations(nums))