tides = int(input())
allTide = list(map(int,(input().split(" "))))
highTide = []
lowTide = []
res = []
allTide.sort()

if tides% 2== 0:
    lowTide=allTide[:tides//2]
    highTide=allTide[tides//2:]
    for i in range(len(highTide)):
        res.append(lowTide[(-i-1)])
        res.append(highTide[i])
else:
    lowTide=allTide[:(tides//2 + 1)]
    highTide=allTide[(tides//2 + 1):]
    for i in range(len(highTide)):
        res.append(lowTide[(-i-1)])
        res.append(highTide[i])
    res.append(lowTide[0])
res = list(map(str, res))

print(' '.join(res))
