
def missingNumber(nums: list[int]) -> int:
    i = 0
    n = len(nums)
    while( i < len(nums)):
        CIndex = nums[i]
        if CIndex != n and nums[i] != nums[CIndex]:
            nums[i],nums[CIndex] = nums[CIndex] , nums[i]
        else:
            i+=1
    
    for i in range(len(nums)):
        if i!= nums[i]:
            return i

nums = [4,0,3,2]
print(missingNumber(nums=nums))