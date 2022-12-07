"""
The Body Mass Index (BMI) is one of the calculations used by doctors to assess an adult's health. The doctor measures the patient's height (in metres) and weight (in kilograms), then calculates the BMI using the formula:

\[BMI = \frac{weight}{height \times height}\]

Write a program which takes the patient's weight and height as input, calculates the BMI, and displays the corresponding message from the table below.
BMI Category 	Message
More than \(25\) 	Overweight
Between \(18.5\) and \(25.0\) (inclusive) 	Normal weight
Less than \(18.5\) 	Underweight
"""

myList = [float(input()), float(input())]

bmi = myList[0]/(myList[1]*myList[1])

if bmi > 25:
    print("Overweight")
elif bmi < 18.5:
    print("Underweight")
else:
    print("Normal weight")
