import sqlite3

conn.execute('''CREATE TABLE CONTACTS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50));''')
print("Table created.")

class Contact:
    # Constructor
    # Defauls row and col to 0 if less than 0
    def __init__(self, id, name, age, address):
        conn.execute("INSERT INTO CONTACTS (ID,NAME,AGE,ADDRESS) \
              VALUES (" + id "," + name + ","+ 28 + "," + address + ")")

        self.id      = get_id(id)
        self.name    = get_name(name)
        self.age     = get_age(age)
        self.address = get_address(address)

    # Getters
    def get_id(self):
        connect()

    def get_name(self):
        connect()

    def get_age(self):
        connect()

    def get_address(self):
        connect()

    # Setters
    def set_id(self, id):
        connect()

    def set_name(self, name):
        connect()


    def set_age(self, age):
        connect()


    def set_address(self, address):
        connect()



    def connect():
        conn = sqlite3.connect("test.db")
        print("Database connected.")


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
table = Table(col, row, headers, border_size)
table.make_table()
table.add_headers(["1", "2", "4"])
print("Here are your current headers: ")
print(table.get_headers())
print("Here is your current border size: ")
print(table.get_border_size())
table.make_table()
table.delete_cols(3, ["1", "2", "4"])
print("Here are your headers now: ")
print(table.get_headers())
print("Let's check your column count: ")
print(table.get_col_count())
# table.delete_cols(4) # should throw error
table.set_row_count(3)
table.add_rows(5)
print("Row count should be 8 because I just set it to 3 and added 5: ")
print(table.get_row_count())
