# dice.py
# Author: René Capella
# Version: 01-14-2022
#
# A die game:
# if on the first turn a player rolls 2, 3, or 12, they lose
# if on the first turn a plater rolls 7 or 11, they will
# other wise, each turn adds points


#Set the turn number to 1
turn_number = 1

#initalize variables to desired starting value: 0. Die roll is set at zero to
# facilitate anticipation of an accurate die roll input
point_number = 0
die_roll = 0

# plater has neither won nor loss, 0 equals not determined
status = 0

# Let the user enter die roll values from a command line. This will allow for controlled
# test data. Eventually, we can convert the die roll to a pseudorandom number for game
# simulations.

while die_roll < 2 or die_roll > 12:
    die_roll_1 = input("Enter the first die roll number (1 to 6): ")



while die_roll < 2 or die_roll > 12:
    die_roll_2 = input("Enter the second die roll number (1 to 6): ")

# cast the string input to an integer
dice_roll_sum = int(die_roll_1)+int(die_roll_2)

# Validate data entry by throwing an error for numerical input <2 or >12.
if dice_roll_sum < 2 or dice_roll_sum > 12:
    raise Exception("Dice total may not be less than 2 or more than 12")

#Die roll is a number from 2 to 12
# While the player has not won or lost, the status is 0
while status == 0 and die_roll < 2 or die_roll > 12:


    # cast the string input to an integer
    die_roll= int(die_roll)

    if turn_number == 1:
        # If turn number = 1 and die roll = 2, 3, or 12, player loses
        if die_roll == 2 or die_roll == 3 or die_roll == 12:
            print("You Lose")
            # update the status to terminate the while
            status = 1
        #If turn number = 1 and die roll = 7 or 11, player wins
        elif die_roll == 7 or die_roll == 11:
            print("You Win!")
            # update the status to terminate the while
            status = 1
        # else if turn number = 1 and die roll not = 2, 3, 7, 11, or 12, point
        # number = die roll and turn number += 1
        else:
            point_number = die_roll
            turn_number += 1
            print("Turn number: " + str(turn_number))
            print("Dice Roll: " + str(die_roll))
            print("Points: " + str(point_number))
            die_roll = 0
    else:
        # If turn number > 1 and die roll = 7 player loses
        if die_roll == 7:
            print("You Lose")
            # update the status to terminate the while
            status = 1
        # If turn number > 1 and die roll = point number player wins
        elif die_roll == point_number:
            print("You Win!")
            # update the status to terminate the while
            status = 1
        # Else turn number +=1
        else:
            turn_number += 1
            print("Turn number: " + str(turn_number))
            print("Dice Roll: " + str(die_roll))
            print("Points: " + str(point_number))
            die_roll = 0

#Print the turn number, the die roll and the result.
print("Turn number: " + str(turn_number))
print("Dice Roll: " + str(die_roll))
print("Points: " + str(point_number))
