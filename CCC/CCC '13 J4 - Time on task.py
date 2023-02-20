time = int(input())
taskTime = []
timeSpent = 0
i = 0

for _ in range(int(input())):
    taskTime.append(int(input()))

taskTime.sort()
while timeSpent <= time:

    timeSpent = timeSpent + taskTime[i]
    if timeSpent > time:
        break
    else:
        i += 1

print(i)
