import os.path
import random

# Functional Requirements
# The solution to the puzzle will be on a text file.
# Setting up
solution            = []
all_correct_guesses = []
output_string       = ""
answer              = ""
selection           = 0
freebie_count       = 0

filename = "solutions.txt"

# Methods
def print_output():
    # Reset the output string
    output_string = ""
    # Build the new output string
    for letter in solution:
        if letter in all_correct_guesses:
            output_string += letter
        else:
            output_string += "_"
    # Print to the user
    print("\n\tHere's your progress: ")
    print("\t", output_string)

def load_word():
    with open("solutions.txt", "r") as file:
        solution_string = file.read().split()[random.randint(0, 19)]
        file.close()

    for char in solution_string:
        solution.append(char)

# Create the file if it doesn't exist
if not os.path.exists(filename):
    file = open("solutions.txt", "w")

    file.write("""pumpkin
    apple
    cucumber
    corn
    pepper
    banana
    yam
    raspberry
    marionberry
    kiwi
    radish
    watermelon
    lime
    strawberry
    gourd
    carrot
    onion
    pear
    orange
    turnip""")


with open("solutions.txt", "r") as file:
        solution_string = file.read().split()[random.randint(0, 19)]
        file.close()

for char in solution_string:
    solution.append(char)

while not output_string == solution_string:
    print("""\n
\t============ Let's Go! =============
\t====================================
            """)

    selection = 0
    while selection < 1 or selection > 5:
        selection = input("""
\tPlease choose an option from the menu below:\n
\t1 - Make a solution guess
\t2 - Guess a letter, please
\t3 - Can I have one freebie letter, please?
\t4 - I give up on this word. May I have another?
\t5 - I give up, I want to go home.
            """)
        print("\n")
        selection = int(selection)

    # 1 - Make a solution guess
    if selection == 1:
        solution_guess = input("What's you solution guess?").lower()
        if solution_guess == solution_string:
            break
        else:
            print("\tNot right yet, friend. Moving on!")
            print("\tPress Enter to continue")
            continue

    # 2 - Guess another letter
    elif selection == 2:
        # The user guesses a letter and enters it on the command line.
        # If the input is greater than one character, prompt repeats
        guess = ""
        while not len(guess) == 1:
            guess = input("Enter your guess (must be a single letter):").lower()

        # add new guess to guesses list
        if guess in solution:
            all_correct_guesses.append(guess)

        # The program tells the user how many times that letter appears in the solution.
        total_frequency = sum(s.count(guess) for s in solution)
        print("\n")
        print("\tThe frequency of your guess in the solution:  ", total_frequency)

        # The program also outputs the partial solution after each guess,
        # showing blank spaces or placeholder characters for letters that have not been
        # correctly guessed yet and showing correctly guessed letters in their accurate
        # places in the solution message.
        print_output()

    # 3 - Can I have a hint, please?
    elif selection == 3:
        random_character = solution_string[random.randint(0, len(solution_string)-1)]
        all_correct_guesses.append(random_character)
        print("\tI've given you the letter ", random_character)

        print_output()

    # 4 - I give up on this word. May I have another.
    elif selection == 4:
        load_word()
        all_correct_guesses = []
        print("\tYour word is reset")
        print_output()
    # 5 - I give up, I want to go home.
    else:
        print("\tOkay, bye! The word was", solution_string)
        quit()

# If guessed, output celebration
print("**************************")
print("******** YOU WIN *********")
