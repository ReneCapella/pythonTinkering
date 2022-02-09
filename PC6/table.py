class Table:
    # Constructor
    # Defauls row and col to 0 if less than 0
    def __init__(self, col_count, row_count, headers = [], border_size = 0):
        self.col_count   = col_count if col_count >= 0 else 0
        self.row_count   = row_count if row_count >= 0 else 0
        self.border_size = border_size if border_size > 0 else 0
        self.headers     = headers

    # Getters
    def get_row_count(self):
        return self.row_count

    def get_border_size(self):
        return self.border_size

    def get_col_count(self):
        return self.col_count

    def get_headers(self):
        return self.headers

    # Setters
    def set_row_count(self, count):
        self.row_count = count

    def set_border_size(self, new_border_size):
        # Pre-Condition: must be between 0 and 5
        if border_size > 5 or border_size < 0:
            raise Exception("Border size must be a number between 0 and 5 inclusively")
        self.border_size = new_border_size

    def set_headers(self, headers):
        # Pre-condition: headers length must be equal to column count
        if len(headers) != self.col_count:
            raise Exception("Headers amount must be the same as column count")
        self.headers = headers

    # Mutators
    def add_rows(self, count):
        # Pre-Condition: count to add must be greater than 0
        if count < 1:
            raise Exception("Number of rows to add must be greater than 0")
        self.row_count += count

    def delete_rows(self, count):
        # Pre-Condition: count to remove must be greater than 0
        if count < 1:
            raise Exception("Number of rows to delete must be greater than 0")
        new_total = self.row_count - count
        self.row_count = new_total if count < self.row_count else 0

    def add_cols(self, col_amt_to_add, headers = []):
        if len(headers) > 0:
            if len(headers) != col_amt_to_add:
                raise Exception("Headers amount must be the same as column count to add")
            self.add_headers(headers)
        else:
            if len(self.headers) > 0:
                raise Exception("Please send through desired header names for columns")
            self.col_count += col_amt_to_add

    def delete_cols(self, col_amt_to_delete, headers = []):
        if len(headers) > 0:
            if len(headers) != col_amt_to_delete:
                raise Exception("Headers amount must be the same as column count to delete")
            self.delete_headers(headers)
        else:
            if len(self.headers) > 0:
                raise Exception("Please send through desired header names for columns removal")
            self.col_count -= col_amt_to_delete

    def add_headers(self, headers):
        self.headers = self.headers + headers
        # Must add the columns if adding Headers
        self.col_count = len(self.headers)

    def delete_headers(self, headers):
        print(headers)
        print(self.headers)
        for header in headers:
            if header in self.headers:
                self.headers.remove(header)
        # Must decrement the column count if removing headers
        self.col_count = len(self.headers)

    def make_table(self):
        reasonable_border = self.border_size > 0
        added_border_element = ["<br>\n","<table border=\"" + str(border_size) +"\">\n"]
        elements    = added_border_element if reasonable_border else ["<br>\n","<table>\n"]
        col_counter = 0
        row_counter = 0

        file = open("table.html", "a")

        if len(self.headers) > 0:
          elements.append("\t<tr>\n")
          for n in self.headers:
             elements.append("\t\t<th>" + n + "</th>\n")
          elements.append("\t</tr>\n")

        while row_counter < self.row_count:
         elements.append("\t<tr>\n")
         while col_counter < self.col_count:
            elements.append("\t\t<td>test</td>\n")
            col_counter += 1
         elements.append("\t</tr>\n")
         row_counter += 1
         col_counter = 0

        elements.append("</table>\n")
        file.writelines(elements)
        file.close()

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
