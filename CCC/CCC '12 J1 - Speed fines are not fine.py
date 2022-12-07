"""
You will output a message for a "radar" sign. The message will display information to a driver based on his/her speed according to the following table:

1 to 20 	    $100
21 to 30 	    $270
31 or above 	$500

The user will be prompted to enter two integers.
First, the user will be prompted to enter the speed limit.
Second, the user will be prompted to enter the recorded speed of the car.

✅ -> Congratulations, you are within the speed limit!
❌ -> You are speeding and your fine is $F. where F is the amount of the fine as described in the table above.
"""
myList = [int(input()), int(input())]
diff = myList[1] - myList[0]

if diff <= 0:
    print("Congratulations, you are within the speed limit!")
if 1 <= diff <= 20:
    print("You are speeding and your fine is $100.")
if 21 <= diff <= 30:
    print("You are speeding and your fine is $270.")
if 31 <= diff:
    print("You are speeding and your fine is $500.")
