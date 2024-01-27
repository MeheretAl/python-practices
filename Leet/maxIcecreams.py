def maxIceCream(costs: list[int], coins: int) -> int:
        maxElement = max(costs)
        icecreams = 0
        freq = [0] * (maxElement + 1)
        for i in range(len(costs)):
            freq[costs[i]]+=1
        
        index = 0
        difference = coins
        for i in range(maxElement+1):
            while freq[i] > 0 :
                costs[index] = i
                difference = difference - index
                if(difference > 0):
                    icecreams +=1
                else:
                    break
                index +=1
                freq[i] -=1
                

        return icecreams

answer = maxIceCream([1,6,3,1,2,5] , 20)
print(answer)