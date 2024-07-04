def digitCount(num: str):
        freq = {}
        for n in num:
            if n in freq:
                freq[int(n)] += 1
            else:
                freq[int(n)] = 1
        
        
        for i in range(len(num)):
            if num[i] != freq[int(num[i])]:
                return False
        return True


nums = "1210"
print(digitCount(nums))