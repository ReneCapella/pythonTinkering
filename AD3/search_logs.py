import re

# Select a file
filename = input("Please enter the filename you'd like to search: ")


# Create a user interface
# The user should be able to enter the name of the file to be searched.

# Check if file exists, please inform user if it does not exist and exit
if not os.path.exists(filename):
    raise Exception("Filename " + filename + " does not exist. Please enter a valid filename")
else
    # The file exists

    # The user should also be able to enter a search character expression.
    txt = input("Please enter the character expression you would like to search for: ")

    # Allow for selected output
    # The user should be able to specify selected output only, such as IP addresses.
    # Select a search term
    selection = input("""
        Please choose an option from the menu below:\n
        1 - Output whole line where match exists
        2 - Output IP Address where match exists if IP is present
        3 - Just give me all the IP addresses
        """)

    # Check the file for the search term line by line
    with open(filename) as f:
        for line in f:
            match = re.search(txt, line)
            if match:
                print(match.string)
