def mergeSort(nums:list[int]) -> list[int]:
    if(len(nums)) <= 1:
        return nums
    
    half = len(nums) // 2

    left = mergeSort([nums[i] for i in range(half)])
    right = mergeSort([nums[i] for i in range(half,len(nums))])

    return merge(left,right)

def merge(first:list[int] , second:list[int]) -> list[int]:
    i = k = j = 0
    mix = [0] * (len(first) + len(second))

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            mix[k] = first[i]
            i+=1
        else:
            mix[k] = second[j]
            j+=1
        k+=1

    while(i < len(first)):
        mix[k] = first[i]
        i+=1
        k+=1
    while(j < len(second)):
        mix[k] = second[j]
        j+=1
        k+=1
    
    return mix


    

nums = [1,9,4,2,1,3,7,4]
print(mergeSort(nums=nums))

