big = {}
counter = 0
breaker = "Waterloo"
lowest = 200

while counter <= 10000:
    city = input()
    if breaker in city:
        ele = city.split(" ")
        big[ele[0]] = int(ele[1])
        break
    else:
        ele = city.split(" ")
        big[ele[0]] = int(ele[1])

for city in big:
    if big[city] < lowest:
        lowest = big[city]
        lowestCity = city

print(lowestCity)
