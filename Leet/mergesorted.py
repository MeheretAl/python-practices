def mergeSorted(nums1:list[int],nums2:list[int]) -> list[int]:

    i = 0
    j = 0
    nums3 = [0] * (len(nums1) + len(nums2))
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            nums3[i+j]  = nums1[i]
            i+=1
        else:
            nums3[i+j] = nums2[j]
            j+=1

    return nums3


 

nums1 = [1,2,3]
nums2 = [2,5,6]

mergeSorted(nums1,nums2)