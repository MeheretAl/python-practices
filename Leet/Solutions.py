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
            
    def longestCommonPrefix(self, strs:list[str]) -> str:
        res = ""
        prefix = strs[0]
        for s in strs:
            prefix = prefix if len(prefix) < len(s) else s
        for i in range(len(prefix)):
            for s in strs:
                if i == len(s) or s[i] != prefix[i]:
                    return res
            res += strs[0][i]
        return res
    
    def romanTonNumeral(self,nums:str) -> int:
        dict = {
            'I':1,'V':5,'X':10,'L':50,
            'C':100,'D':500,'M':1000
        }

        res = 0
        for i in range(len(nums)):
            if i+1 < len(nums) and dict[nums[i]] < dict[nums[i+1]]:
                res -= dict[nums[i]]
            else:
                res += dict[nums[i]]
        
        return res
    
    def search2dMatrix(self,matrix:list[list[int]],target:int) -> bool:
        arr = []
        for i in matrix:
            for j in i:
                arr.append(j)
        #there is a better way to do this with binary search on the 2D matrix itself
        #i just converted the 2D matrix into a one dimensional array then searched through that list
        return False if target not in arr else True
