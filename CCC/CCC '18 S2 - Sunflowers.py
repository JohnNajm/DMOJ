def check(initial):
    if initial[0][0] < initial[-1][-1] and sorted(initial[0]) == initial[0] and initial[0][0] < initial[-1][0]:
        for r in initial:
            for c in r:
                print(c,end = " ")
            print()
    else:
        rotated = [list(reversed(col)) for col in zip(*initial)]
        check(rotated)

rows = int(input())
flowers = []
for i in range(rows):
    add = []
    add = list(map(int,(input().split(" "))))
    flowers.append(add)

check(flowers)