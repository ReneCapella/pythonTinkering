import csv
import os.path

# Create a Python program that reads data from a CSV file
# and presents it to the console.

def pad_col(col, max_width):
    return col.ljust(max_width)

file_name = ""
while not os.path.exists(file_name):
    file_name = input("Hello, there. Tell me a name of a CSV file that exists in this directory, please: ")


headers = ""
with open(file_name) as csvfile:
    reader = csv.reader(csvfile)
    all_rows = []
    for row in reader:
        all_rows.append(row)
    headers = all_rows[0]
max_col_width = [0] * len(all_rows[0])
for row in all_rows:
    for idx, col in enumerate(row):
        max_col_width[idx] = max(len(col), max_col_width[idx])

for row in all_rows:
    to_print = ""
    for idx, col in enumerate(row):
        to_print += pad_col(col, max_col_width[idx]) + " | "
    print("-"*len(to_print))
    print(to_print)


# Then add a feature to allow for entering additional data on the console
# and appending the new data to the original CSV file.

add = ""
while add != "Y" and add != "N":
    add = input("Do you want to add information to this csv? Y/N: ")

if add == "Y":
    to_add = []
    for header in headers:
        phrase = "Enter the information for column: " + header + " "
        answer = input(phrase)

        to_add.append(answer)

    with open(file_name, mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(to_add)
        employee_file.write("\n")
else:
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile)
        all_rows = []
        for row in reader:
            all_rows.append(row)
            for field in row:
            if field == "Harper Lee"

                all_rows.remove(row)


print("Okie Dokie, Artichokie: see you later!")
