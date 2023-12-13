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