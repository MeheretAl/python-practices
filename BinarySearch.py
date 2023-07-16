#binary search using recursive method

def binarySearchAlgorithm(array,target):
    return binarySearch(array,0,len(array)-1,target)

def binarySearch(array,left,right,target):
    while left <= right:
        mid = int((left+right)/2)
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right =mid-1
    return left

#example
binarySearchAlgorithm(array = [x for x in range(1,76)],target=54)