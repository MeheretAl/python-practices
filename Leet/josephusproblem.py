# def findTheWinner(n:int,k:int) -> int:
#    
#     nums = [x+1 for x in range(n)]
#     if len(nums) == 1:
#         return nums[0] 
#     #base case
#     #return the only element left in the list

#     #circular array
#     nextIndex = ((n + k) % len(nums))
#     #remove the value at the kth index
#     nums.remove(nums.index(k))

#     return findTheWinner(nextIndex,k)

#     #recursive function works when the list is explicitly given

def findTheWinner(nums:list[int],start:int,k:int) -> int:
    # generate list from 1 to n inclusive
    # [1,2,3,4,5]
    # k is for the steps taken to remove person
    # k = 2 in this example means
    # [1,2,3,4,5] go 1 then 2 (2 steps) remove 2
    # [1,3,4,5] go 3 then 4 remove 4
    # [1,3,5] go 5 then 1
    # [3,5] go 3 then 5
    # [3] return 3

    if len(nums) == 1:
        return nums[0]
    #base case for the recursion
    
    #circular array
    nextIndex = (start + k-1) % len(nums)
    #removing kth element
    nums.pop(nextIndex)
    #recursive call
    return findTheWinner(nums,nextIndex,k)

def noRecurse(n:int,k:int) -> int:
    nums = [x+1 for x in range(n)]
    nextIndex = 0
    while len(nums) > 1:
        currSize = len(nums)
        nextIndex = (nextIndex + k - 1) % currSize
        del nums[nextIndex]
        
        

    return nextIndex

print(noRecurse(5,2))




# check  = [1,2,3,4,5]
# print(findTheWinner(check,0,2))