"""
You would like to do some experiments in natural language processing. Natural language processing (NLP) involves using machines to recognize human languages.

Your first idea is to write a program that can distinguish English text from French text.

After some analysis, you have concluded that a very reasonable way of distinguishing these two languages is to compare the occurrences of the letters t and T to the occurrences of the letters s and S. Specifically:

    if the given text has more t and T characters than s and S characters, we will say that it is (probably) English text;
    if the given text has more s and S characters than t and T characters, we will say that it is (probably) French text;
    if the number of t and T characters is the same as the number of s and S characters, we will say that it is (probably) French text.

"""
N = int(input())
textList = []
s_count = 0
t_count = 0

for i in range(N):
    textList.append(str(input()))
    for char in range(len(textList[i])):
        if textList[i][char] == "s" or textList[i][char] == "S":
            s_count += 1
        if textList[i][char] == "t" or textList[i][char] == "T":
            t_count += 1

if s_count >= t_count:
    print("French")
else:
    print("English")
