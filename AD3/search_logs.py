import re
import os.path

# Select a file
filename = input("Please enter the filename you'd like to search: ")

# Create a user interface
# The user should be able to enter the name of the file to be searched.

# Check if file exists, please inform user if it does not exist and exit
if not os.path.exists(filename):
    raise Exception("Filename does not exist. Please enter a valid filename")
else:
    selection = 0
    while selection < 1 or selection > 3:
        selection = input("""
            Please choose an option from the menu below:\n
            1 - Output whole line where match exists
            2 - Output IP Address where match exists if IP is present
            3 - Just give me all the IP addresses
            """)
        selection = int(selection)

    with open(filename) as file:
        fi = file.readlines()

    if selection == 1:
        txt = input("Please enter the character expression you would like to search for: ")
        # Check the file for the search term line by line
        for line in fi:
            match = re.search(txt, line)
            if match:
                print(match.string)
    elif selection == 2:
        txt = input("Please enter the character expression you would like to search for: ")
        # Output IP addresses on lines that match the search criteria
        ip_pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        for line in fi:
            match = re.search(txt, line)
            ip = re.findall(ip_pattern,line)
            if match and ip:
                print(ip)
    else:
        # Output all IP addresses in the file
        ip_pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

        for line in fi:
            ip = re.findall(ip_pattern,line)
            if ip:
                print(ip)
