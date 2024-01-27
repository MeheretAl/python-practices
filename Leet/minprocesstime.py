
def minProcessingTime(processorTime: list[int], tasks: list[int]) -> int:
        pTime = len(processorTime)
        tasklength = len(tasks)
        interval = tasklength//pTime
        tasks.sort()
        processorTime.sort(reverse = True)

        ans = 0

        for i in range(pTime):
            currentMax = processorTime[i] + tasks[(i + 1) * interval - 1]
            ans = max(currentMax, ans)
                     

        return ans

processorTime = [8,10]
tasks = [2,2,3,1,8,7,4,5]

ans = minProcessingTime(processorTime=processorTime,tasks=tasks)

print(ans)

