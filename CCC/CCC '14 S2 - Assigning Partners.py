wled = int(input())

list1 = str(input()).split()
list2 = str(input()).split()

res = 1

if len(list1) != len(list2):
    print("bad")

else:
    dict={}
    for i in range(wled):
        if list2[i] in dict:
            if dict[list2[i]] == list1[i]:
                continue
            else:
                res = 0
                break
        else:
            if list1[i] == list2[i]:
                res = 0
                break
            else:
                dict[list1[i]] = list2[i]

if res == 1:
    print("good")
else:
    print("bad")