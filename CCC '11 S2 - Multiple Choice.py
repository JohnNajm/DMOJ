N = int(input())
studentAnswers = []
correctAnswers = []
counter = 0
for _ in range(N):
    studentAnswers.append(input())
for _ in range(N):
    correctAnswers.append(input())

for i in range(N):
    if studentAnswers[i] == correctAnswers[i]:
        counter += 1

print(counter)
