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