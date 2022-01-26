import os.path

# Functional Requirements
# The solution to the puzzle will be on a text file.


# Reads only the first word in a file
filename = open("solution.txt", "r")

if os.path.exists(filename):
    with open("solution.txt", "r") as file:
            solution_string = file.read().split()[0]
    f.close()
else:
    raise Exception("Please create a file named solution.txt with at lease one word")

solution = []
all_correct_guesses = []
output_string = ""
answer = ""

for char in solution_string:
    solution.append(char)

while not output_string == solution_string:
    print("============ Let's Go! =============")
    print("====================================")

    # The user guesses a letter and enters it on the command line.
    # If the input is greater than one character, prompt repeats
    guess = ""
    while not len(guess) == 1
        guess = input("Enter your guess (must be a single letter):")

    # add new guess to guesses list
    if guess in solution:
        all_correct_guesses.append(guess)

    # The program tells the user how many times that letter appears in the solution.
    total_frequency = sum(s.count(guess) for s in solution)
    print("The frequency of your guess in the solution:  ", total_frequency)

    # The program also outputs the partial solution after each guess,
    # showing blank spaces or placeholder characters for letters that have not been
    # correctly guessed yet and showing correctly guessed letters in their accurate
    # places in the solution message.

    # Reset the output string
    output_string = ""
    # Build the new output string
    for letter in solution:
        if letter in all_correct_guesses:
            output_string += letter
        else:
            output_string += "_"
    # Print to the user
    print(output_string)

# If guessed, output celebration
print("**************************")
print("******** YOU WIN *********")
