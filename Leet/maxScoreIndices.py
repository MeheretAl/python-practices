def maxScoreIndices(nums:list[int]) -> list[int]:
    
    finalAnswer = [0] #for some edgecases
    
    rightCount = 0 
    # maxSum is atleast equal to the number of 1's in the right side of the array
    # when we're at the first iteration of nums where nums =[0,0,1,0]
    # numsLeft = [] numsRight = [0,0,1,0]
    # maxSum is at least equal to 1
    # we could also go the other way around starting from the end 
    # numsright = [], numsleft = [0,0,1,0]-> 3
    # meaning the maxSum is atleast equal to 3
    # but the loop is more straightforward starting from the right
    for num in nums:
        if num == 1:
            rightCount +=1
    #calculating rightCount here
    
    leftCount = 0
    maxAnswer = rightCount #assigned rightCount to maxAnswer 
    for i in range(len(nums)):
        if nums[i] == 0:
            leftCount += 1
        else:
            rightCount -= 1 #when we find 1 that means we're past the index so decrement it
                # [0,0,1,0] reaching 1 means numsleft = [0,0,1] and numsRight = [0]
                # so leftCount = 2 and rightCount = 1-1 = 0 which is correct
                # leftnum has 2 zeroes -> leftCount = 2 and right count is zero because numsRight = [0]

        currentVal = leftCount +rightCount
        #the current sum is calculated here
        #assuming we're on the 2nd index currentVal = 2 + 1 = 3 
        if currentVal == maxAnswer:      
            finalAnswer.append(i+1)
            # add the index+1 to the answer if our current iteration is equal to the maxVal
        elif currentVal >maxAnswer:
            #we've found a new max therefore remove the old values and update it
            finalAnswer = []
            finalAnswer.append(i+1)
            #new max therfore maxAnswer is the new max aka currentVal
            maxAnswer = currentVal

    return finalAnswer