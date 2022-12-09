"""
Martha takes a jar of quarters to the casino with the intention of becoming rich. She plays three machines in turn. Unknown to her, the machines are entirely predictable. Each play costs one quarter. The first machine pays \(30\) quarters every \(35^{th}\) time it is played; the second machine pays \(60\) quarters every \(100^{th}\) time it is played; the third pays \(9\) quarters every \(10^{th}\) time it is played.
Input Specification

Your program should take as input the number of quarters in Martha's jar (there will be at least one and fewer than \(1000\)), and the number of times each machine has been played since it last paid.
Output Specification

Your program should output the number of times Martha plays until she goes broke.
"""
quarters = int(input())
a = int(input())
b = int(input())
c = int(input())
plays = 0

while quarters > 0:

    if quarters > 0:
        quarters -= 1
        a += 1
        if a % 35 == 0:
            quarters += 30
        plays += 1

    if quarters > 0:
        quarters -= 1
        b += 1
        if b % 100 == 0:
            quarters += 60
        plays += 1

    if quarters > 0:
        quarters -= 1
        c += 1
        if c % 10 == 0:
            quarters += 9
        plays += 1


print("Martha plays ", plays, " times before going broke.")
