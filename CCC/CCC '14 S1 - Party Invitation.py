"""
Canadian Computing Competition: 2014 Stage 1, Junior #4, Senior #1

You are hosting a party and do not have room to invite all of your friends. You use the following unemotional mathematical method to determine which friends to invite.

Number your friends \(1, 2, \dots, K\) and place them in a list in this order. Then perform \(m\) rounds. In each round, use a number to determine which friends to remove from the ordered list.

The rounds will use numbers \(r_1, r_2, \dots, r_m\). In round \(i\) remove all the remaining people in positions that are multiples of \(r_i\) (that is, \(r_i, 2r_i, 3r_i, \dots\)) The beginning of the list is position \(1\).

Output the numbers of the friends that remain after this removal process.
Input Specification

The first line of input contains the integer \(K\) \((1 \le K \le 100)\). The second line of input contains the integer \(m\) \((1 \le m \le 10)\), which is the number of rounds of removal. The next \(m\) lines each contain one integer. The \(i^{th}\) of these lines \((1 \le i \le m)\) contains \(r_i\) \((2 \le r_i \le 100)\) indicating that every person at a position which is multiple of \(r_i\) should be removed.
Output Specification

The output is the integers assigned to friends who were not removed. One integer is printed per line in increasing sorted order.
"""
attendees = []
rem = []

l = int(input())
for i in range(0, l):
    attendees.append(i+1)

n = int(input())
for _ in range(n):
    index = int(input())
    # finds every n-th element and creates a list of their respective indexes
    for ind, ele in enumerate(attendees):
        if (ind+1) % index == 0:
            rem.append(ind)

    # pops elements from attendees in reversed order
    for z, x in enumerate(reversed(rem)):
        attendees.pop(x)
    rem = []

for p in range(len(attendees)):
    print(attendees[p])
