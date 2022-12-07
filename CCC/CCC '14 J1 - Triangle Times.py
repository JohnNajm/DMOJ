"""
You have trouble remembering which type of triangle is which. You write a program to help. Your program reads in three angles (in degrees).

    If all three angles are \(60\), output Equilateral.
    If the three angles add up to \(180\) and exactly two of the angles are the same, output Isosceles.
    If the three angles add up to \(180\) and no two angles are the same, output Scalene.
    If the three angles do not add up to \(180\), output Error.

Input Specification

The input consists of three integers, each on a separate line. Each integer will be greater than \(0\) and less than \(180\).
Output Specification

Exactly one of Equilateral, Isosceles, Scalene or Error will be printed on one line.
"""
myList = [int(input()), int(input()), int(input())]
myList.sort()

if sum(myList) != 180:
    print("Error")
else:
    if myList[0] == myList[1] == myList[2]:
        print("Equilateral")
    elif myList[0] == myList[1] or myList[1] == myList[2]:
        print("Isosceles")
    else:
        print("Scalene")
