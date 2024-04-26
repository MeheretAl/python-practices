
def findIntersectionValues(nums1: list[int], nums2: list[int]) -> list[int]:
        #store all of nums1 in a map
        freq1 = {}
        countI = 0 
        freq2 = {}
        countJ = 0
        for i in range(len(nums1)):
            if nums1[i] in freq1:
                freq1[nums1[i]]+=1
            else:
                freq1[nums1[i]] = 1
        for j in range(len(nums2)):
            if nums2[j] in freq2:
                freq2[nums2[j]] += 1
            else:
                freq2[nums2[j]] = 1
        for num in freq1:
            if num in freq2:
                countI += freq1[num]
        
        for num in freq2:
            if num in freq1:
                countJ += freq2[num]
        
        return [countI,countJ]
