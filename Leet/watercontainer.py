def maxArea(height : list[int]) -> int:
    start = 0
    end = len(height) - 1
    maxArea = (end - start) * height[0]
    while start < end:
        area = (end-start) * min(height[start],height[end])
        maxArea = max(area,maxArea)
        if(height[start]>height[end]):
            end -=1
        else:
            start+=1

    
    return maxArea

height = [1,8,6,2,5,4,8,3,7]
answer = maxArea(height)
print(answer)