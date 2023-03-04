directions = []
while True:
    line = str(input())
    if line == "R":
        directions.append("LEFT")
    elif line == "L":
        directions.append("RIGHT")
    elif line == "SCHOOL":
        break
    else:
        directions.append(line)

directions.reverse()

for ind,ele in enumerate(directions):
    if ind%2 ==0 and ind < len(directions)-1:
        print("Turn " + ele + " onto " + directions[ind+1] + " street.")
print("Turn " + directions[-1] + " into your HOME.")