"""
Input Specification

The first line will contain an integer \(N\) \((1 \le N \le 100\,000)\), the number of addition problems Tudor needs to do. The next \(N\) lines will each contain two space-separated integers whose absolute value is less than \(1\,000\,000\,000\), the two integers Tudor needs to add.
Output Specification

Output \(N\) lines of one integer each, the solutions to the addition problems in order.

"""
N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    print(a + b)
