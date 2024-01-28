def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    unique = set()
    nums1.sort()
    nums2.sort()
    pt1 = pt2 = 0

    while pt1<len(nums1) and pt2 < len(nums2):
        if nums1[pt1] == nums2[pt2]:
            unique.add(nums1[pt1])
            pt1+=1
            pt2+=1
        elif nums1[pt1] < nums2[pt2]:
            pt1+=1
        else:
            pt2+=1
    
    return list(unique)

nums1 = [1,2]
nums2 = [2,1]
answer = intersection(nums1,nums2)
print(answer)