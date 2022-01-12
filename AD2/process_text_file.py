import os
import os.path
################### SET UP #######################
# create the file at runtime so it doesn't need set up
# if it isn't in the directory
if not os.path.exists("Project2Input.txt"):
    file = open("Project2Input.txt", "w")
    file.write("""Test input file for Project 2.
Add some test to this file.
-------------------------------\n""")
    file.close()

################## Main Program ##################
# Opens a given file for appending
file = open("Project2Input.txt", "a")

# Lets the user add text to the file through command line input
text_to_append = input("Enter the text you want to add to the file: ")
file.write(text_to_append)
file.close()

# Saves a copy of the file with a different file name
os.system('cp Project2Input.txt Project2Update.txt')

# Deletes the original file
os.remove("Project2Input.txt")
