"""
Canadian Computing Competition: 2013 Stage 1, Junior #3, Senior #1

You might be surprised to know that 2013 is the first year since 1987 with distinct digits. The years 2014, 2015, 2016, 2017, 2018, 2019 each have distinct digits. 2012 does not have distinct digits, since the digit 2 is repeated.

Given a year, what is the next year with distinct digits?
Input Specification

The input consists of one integer \(Y\) (\(0 \le Y \le 10\,000\)), representing the starting year.
Output Specification

The output will be the single integer \(D\), which is the next year after \(Y\) with distinct digits.
"""
def distinct(yr):
    s = str(yr)
    for digit in s:
        if s.count(digit) > 1:
            return False
    return True


year = int(input()) + 1
while not distinct(year):
    year = year + 1

print(year)
