class Solutions:
    #inefficient method but will do for the time being
    #will come back after learning binary search in depth
    def searchInsert(self,nums: list[int],target:int) -> int: 
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        
    def binarysearch(self,my_list:list[int],target:int):
        left,right = 0 , len(my_list)
        while left < right:
            mid = (left +right)//2
            if my_list[mid] < target:
                left = mid
            elif my_list[mid] > target:
                right = mid
            else:
                return mid
            
    def 