def smaller(nums:list[int]) -> list[int]:
    count = [0] * (max(nums) + 1)

    #get the freq of each number in the list
    for num in nums:
        count[num] += 1

    cumulative = [0] * (max(nums) + 2)
    prevSum = 0
    #calculate the cumulative freq of each number in nums
    #needed to find the position of each num in the sorted list
    for i in range(len(count)):
        prevSum += count[i]
        cumulative[i+1] = prevSum
    #ans array to store the final answer
    ans = [0] * len(nums)
    for i in range(len(ans)):
        ans[i] = cumulative[nums[i]]
    
    return ans

    #given [8,1,2,2,3]
    '''
    count looks like this [0,1,2,1,0,0,0,0,1]
    cumulative count looks like this [0, 0, 1, 3, 4, 4, 4, 4, 4, 5]
    for i in range(len(ans)):
        ans[i] = cumulative[nums[i]]
    this part does ans[0] = cumulative[nums[0]] -> cumulative[8] -> 4
    ans[0] = 4
    ans[1] = cumulative[1] = 0
    ans[2] = cumulative[2] = 1
    ans[3] = cumulative[2] = 1
    ans[4] = cumulative[3] = 3
    ans = [4,0,1,1,3] 
    ''' 

nums = [8,1,2,2,3]
smaller(nums)


    


smaller([8,1,2,2,3])

