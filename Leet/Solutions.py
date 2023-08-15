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
