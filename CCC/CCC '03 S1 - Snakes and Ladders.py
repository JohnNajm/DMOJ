"""
When the program starts it should assume the piece is on square \(1\). It should repeatedly read input from the user (a number between \(2\) and \(12\)) and report the number of the square where the piece lands. In addition, if the piece moves to the last square, the program should print You Win! and terminate. If the user enters 0 instead of a number between 2 and 12, the program should print You Quit! and terminate.

For clarity, you are to use the board pictured above and you should note that the board has \(3\) snakes (from \(54\) to \(19\), from \(90\) to \(48\) and from \(99\) to \(77\)) and 3 ladders (from \(9\) to \(34\), from \(40\) to \(64\) and from \(67\) to \(86\)).
"""
current_pos = 1
modifiers = [54, 90, 99, 9, 40, 67]
to = [19, 48, 77, 34, 64, 86]

while current_pos != 100 and current_pos < 100:
    dice = int(input())
    if dice == 0:
        print("You Quit!")
        break
    elif dice + current_pos > 100:
        print("You are now on square ", current_pos)
    else:
        current_pos = current_pos + dice
        if current_pos in modifiers:
            current_pos = to[modifiers.index(current_pos)]
        print("You are now on square ", current_pos)

print("You Win!")
