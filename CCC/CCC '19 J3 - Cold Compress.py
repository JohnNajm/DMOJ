lines = int(input())

for i in range(lines):
    string = str(input())
    zebbe = []
    zebbe.append(0)

    for s in string:
        if zebbe[-1] == s:
            zebbe[-2] += 1
        else:
            zebbe.append(1)
            zebbe.append(s)

    zebbe.pop(0)
    mystring = ' '.join(map(str,zebbe))
    print(mystring)