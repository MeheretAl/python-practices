def goodpairs(nums: list[int]) -> int:
    dict1 = {}
    counter = 0
    for i in range(len(nums)):
        if nums[i] in dict1:
            counter += dict1[nums[i]]
            dict1[nums[i]] += 1
        else:
            dict1[nums[i]] = 1

    return counter
