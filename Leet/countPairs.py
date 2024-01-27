def countPairs(nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            if(nums[start] + nums[end] < target and start!=end):
                ans +=1
                end -=1
            else:
                end -= 1
        
        return ans

nums = [-1,3,2,1,1]
target = 2

ans = countPairs(nums,target)
print(ans)