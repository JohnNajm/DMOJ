"""
There will be one line of input that contains between \(1\) and \(255\) characters.

The output is determined by the following rules:

    If the input line does not contain any happy or sad emoticons, output none.
    Otherwise, if the input line contains an equal number of happy and sad emoticons, output unsure.
    Otherwise, if the input line contains more happy than sad emoticons, output happy.
    Otherwise, if the input line contains more sad than happy emoticons, output sad.

"""
string = str(input())
happyCounter = 0
sadCounter = 0

for i in range(len(string)-2):
    if string[i:i+3] == ":-)":
        happyCounter = happyCounter + 1
    elif string[i:i+3] == ":-(":
        sadCounter = sadCounter + 1

if happyCounter == 0 and sadCounter == 0:
    print("none")
elif happyCounter == sadCounter:
    print("unsure")
elif happyCounter > sadCounter:
    print("happy")
else:
    print("sad")
