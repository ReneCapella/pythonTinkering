# dice.py
# Author: René Capella
# Version: 01-14-2022
#
# A die game:
# if on the first turn a player rolls 2, 3, or 12, they lose
# if on the first turn a plater rolls 7 or 11, they will
# other wise, on turns after 1, rolling 7 loses, rolling equal to points, wins
# otherwise, turn advances

#Set the turn number to 1
turn_number = 1

#initalize variables to desired starting value: 0
point_number = 0
die_roll_1 = 0
die_roll_2 = 0

# Let the user enter die roll values from a command line. This will allow for controlled
# test data. Eventually, we can convert the die roll to a pseudorandom number for game
# simulations.

#Die roll is a number from 1 to 6
while die_roll_1 < 1 or die_roll_1 > 6:
    die_roll_1 = input("Enter the first die roll number (1 to 6): ")
    die_roll_1 = int(die_roll_1)
    if die_roll_1 < 1 or die_roll_1 > 6:
        print("Die roll must be from 1 to 6, Try again")

while die_roll_2 < 1 or die_roll_2 > 6:
    die_roll_2 = input("Enter the second die roll number (1 to 6): ")
    die_roll_2 = int(die_roll_2)
    if die_roll_2 < 1 or die_roll_2 > 6:
        print("Die roll must be from 1 to 6, Try again")

# cast the string input to an integer
dice_roll_sum = int(die_roll_1) + int(die_roll_2)

# Validate data entry by throwing an error for numerical input <2 or >12.
if dice_roll_sum < 2 or dice_roll_sum > 12:
    raise Exception("Dice total may not be less than 2 or more than 12")

if turn_number == 1:
    # If turn number = 1 and die roll = 2, 3, or 12, player loses
    if dice_roll_sum == 2 or dice_roll_sum == 3 or dice_roll_sum == 12:
        print("==============================")
        print("YOU LOSE")
        print("==============================")
    #If turn number = 1 and die roll = 7 or 11, player wins
    elif dice_roll_sum == 7 or dice_roll_sum == 11:
        print("==============================")
        print("YOU WIN!")
        print("==============================")
    # else if turn number = 1 and die roll not = 2, 3, 7, 11, or 12, point
    # number = die roll and turn number += 1
    else:
        point_number = dice_roll_sum
        turn_number += 1

# This will only run if and when the turn number advances to turn #2
if turn_number > 1:
    print("==============================")
    print("NEXT TURN")
    print("==============================")

    # if I were writing this officially, I would make this a function
    # Die roll is a number from 2 to 12
    die_roll_1 = input("Enter the first die roll number (1 to 6): ")
    die_roll_2 = input("Enter the second die roll number (1 to 6): ")
    # cast the string input to an integer
    dice_roll_sum = int(die_roll_1)+int(die_roll_2)

    # Validate data entry by throwing an error for numerical input <2 or >12.
    if dice_roll_sum < 2 or dice_roll_sum > 12:
        raise Exception("Dice total may not be less than 2 or more than 12")

    # if dice roll equals 7, you lose: then it prints the roll stats
    if dice_roll_sum == 7:
        print("==============================")
        print("YOU LOSE")
        print("==============================")
    # If turn number > 1 and die roll = point number player wins, : then it prints the roll stats
    elif dice_roll_sum == point_number:
        print("==============================")
        print("YOU WIN!")
        print("==============================")
    # Else turn number +=1
    else:
        turn_number += 1

#Print the turn number, the die roll and the result.
print("==============================")
print("GAME STATS")
print("==============================")
print("Turn number: " + str(turn_number))
print("Dice Roll: " + str(dice_roll_sum))
print("Points: " + str(point_number))
