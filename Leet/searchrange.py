def searchRange(self,nums:list[int],target:int) -> list[int]:
        left_most,right_most = -1,-1
        left,right = 0, len(nums) - 1
        while (left <= right):
            mid = (left+right)//2
            if nums[mid]==target:
                left_most = mid
                right = mid -1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid +1
        
        
        if left_most == -1: return [-1,-1]

        left,right = 0,len(nums) -1
        while (left<=right):
            mid =(left+right)//2
            if nums[mid] == target:
                right_most = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return [left_most,right_most] if right_most != -1 else [-1,-1]