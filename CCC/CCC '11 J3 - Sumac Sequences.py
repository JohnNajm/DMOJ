def summac(int1, int2):
    res = int1 - int2
    return res


List = [int(input()), int(input())]

while List[-2] >= List[-1]:
    List.append(summac(List[-2], List[-1]))

print(len(List))






