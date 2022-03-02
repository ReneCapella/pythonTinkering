# Take code from one of your previous assignments and use it to create one or modules.
# Upload a .zip file including your module(s) and some test code that calls your modules.
# To earn credit for this assignment, a tester should be able to:

# download your files

# extract your files

# launch the test code in a Python environment

# see results without errors

import table

col      = 0
row      = 0
header   = ""
headers  = []
border_size = -1

while col < 1 or col > 100:
    col = input("How many columns do you want (1 to 100)? ")
    col = int(col)

while row < 1 or col > 100:
    row = input("How many rows do you want (1 to 100)? ")
    row = int(row)

while header != "Y" and header != "N":
    header = input("Do you want headers? Y/N ")

# If headers are wanted, give them names
if header == "Y":
    header = True
    for n in range(col):
        headers.append(input("Header #" + str(n + 1) + ": "))
else:
    header = False

while border_size < 0 or border_size > 5:
    border_size = input("Enter a number for border size 1 to 5 ")
    border_size = int(border_size)

# DEMOOOOOO
print(border_size)
table_to_create = table.Table(col, row, headers, border_size)
table_to_create.make_table()
table_to_create.add_headers(["1", "2", "4"])
print("Here are your current headers: ")
print(table_to_create.get_headers())
print("Here is your current border size: ")
print(table_to_create.get_border_size())
table_to_create.make_table()
table_to_create.delete_cols(3, ["1", "2", "4"])
print("Here are your headers now: ")
print(table_to_create.get_headers())
print("Let's check your column count: ")
print(table_to_create.get_col_count())
# table_to_create.delete_cols(4) # should throw error
table_to_create.set_row_count(3)
table_to_create.add_rows(5)
print("Row count should be 8 because I just set it to 3 and added 5: ")
print(table_to_create.get_row_count())
