import os.path

# Create a Python function to output a HTML table. The function should have parameters
# for number of rows, number of columns, header row (yes/no).

# Your deliverable is to turn in your code as a .py file. For full credit, the code
# needs to test successfully in my environment.

# Here is some starter code. Add features to this.

####################
# METHODS
####################
def make_table(row, col, header):
    elements = []
    col_count = 0
    row_count = 0

    # if a table already exists, add a breakline and append new table under
    if os.path.exists("table.html"):
        elements.append("<br>\n")

    file = open("table.html", "a")

    elements.append("<table>\n")
    if len(headers) > 0:
      elements.append("\t<tr>\n")
      for n in headers:
         elements.append("\t\t<th>" + n + "</th>\n")
      elements.append("\t</tr>\n")

    while row_count < row:
     elements.append("\t<tr>\n")
     while col_count < col:
        elements.append("\t\t<td>test</td>\n")
        col_count += 1
     elements.append("\t</tr>\n")
     row_count += 1
     col_count = 0

    elements.append("</table>\n")
    file.writelines(elements)
    file.close()

####################
# INTERFACE
####################
col      = 0
row      = 0
header   = ""
headers  = []

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

make_table(row, col, header)
