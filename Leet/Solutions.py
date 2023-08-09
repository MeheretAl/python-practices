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
