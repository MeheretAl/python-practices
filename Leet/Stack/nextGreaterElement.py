def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
        #O(n) solution
        indexMap = {}
        ans = [-1] * len(nums1)
        stack = []
        #storing the index
        for i in range(len(nums1)):
            indexMap[nums1[i]] = i

        for i in range(len(nums2)):
            num = nums2[i]
            while stack and num > stack[-1]:
                val = stack.pop()
                index = indexMap[val]
                ans[index] = num
            if num in indexMap:
                stack.append(num)

        return ans

nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1,nums2))