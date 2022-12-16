"""
Question 1: what is the minimum total speed, out of all possible assignments into pairs?
Question 2: what is the maximum total speed, out of all possible assignments into pairs?

Input Specification
The first line will contain the type of question you are to solve, which is either \(1\) or \(2\).

The second line will contain \(N\) \((1 \le N \le 100)\).

The third line will contain \(N\) space-separated integers: the speeds of the citizens of Dmojistan.

The fourth line will contain \(N\) space-separated integers: the speeds of the citizens of Pegland.

Each person's speed will be an integer between \(1\) and \(1\,000\,000\).

For 8 of the 15 available marks, questions of type \(1\) will be asked. For 7 of the 15 available marks, questions of type \(2\) will be asked.

Output Specification
Output the maximum or minimum total speed that answers the question asked.
"""
q = int(input())
n = int(input())
dmoj = list(input().split(" "))
peg = list(input().split(" "))
dmoj = list(map(int, dmoj))
peg = list(map(int, peg))
def q1(l1, l2):
    dmoj.sort()
    peg.sort()
    ans = 0
    for i in range(n):
        if l1[i] > l2[i]:
            ans = ans + int(l1[i])
        else:
            ans = ans + int(l2[i])
    return ans
def q2(l1, l2):
    dmoj.sort()
    peg.sort(reverse=True)
    ans = 0
    for i in range(n):
        if l1[i] > l2[i]:
            ans = ans + int(l1[i])
        else:
            ans = ans + int(l2[i])
    return ans


if q == 1:
    print(q1(dmoj, peg))
else:
    print(q2(dmoj, peg))

"""
202 177 189 589 102
17 78 1 496 540
"""
