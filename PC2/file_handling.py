
# Author:  René Capella
# Version: 01/11/2022
#
# This file contains 4 programs: create, write to, append to, and delete a File
# Also demostrated is file handing in other directories
# To properly use this file, please comment out sections as needed


# create a file program
open("write_to_me/whoohoo.txt", "x")

#write to a file program
open("write_to_me/whoohoo.txt", "x")
written_file = open("write_to_me/whoohoo.txt", "w")
for char in "whoohoo":
    written_file.write(char.upper())

# #append to a file program
appended_file = open("write_to_me/whoohoo.txt", "a")
appended_file.write("\nFile Handling!")

# #delete a File program
import os

open("write_to_me/whoohoo.txt", "x")
os.remove("write_to_me/whoohoo.txt")
