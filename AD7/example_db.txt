# As a deliverable for this assignment, screen shots and/or text file copies of
# the queries ... will be enough. If you get the proper query results, I will
# assume your Python code is working well. (For troubleshooting requests, please
# also upload the code!)

import sqlite3
conn = sqlite3.connect("test.db")
print("Database connected.")

# Create a table in the test database.
print("\nCreating a table in the test database")
conn.execute('''CREATE TABLE CONTACTS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50));''')
print("\nTable created.")

conn.close()

# Add some records to the table.
conn = sqlite3.connect("test.db")
print("\nAdding some records to the table")
conn.execute("INSERT INTO CONTACTS (ID,NAME,AGE,ADDRESS) \
      VALUES (10, 'Polly', 32, 'Seattle')")

conn.execute("INSERT INTO CONTACTS (ID,NAME,AGE,ADDRESS) \
      VALUES (11, 'Roger', 28, 'Bainbridge')")

conn.commit()
print("Records created.")
conn.close()

# Search the table for a specific record.
conn = sqlite3.connect("test.db")
print("\nHere are all the records:")
cursor = conn.execute("SELECT * from CONTACTS")
for row in cursor:
    print("ID = " + str(row[0]))
    print("NAME = " + row[1])
    print("AGE = " + str(row[2]))
    print("ADDRESS = " + str(row[3]) + "\n")

conn.close()


# Update a record in the table.
conn = sqlite3.connect("test.db")
print("\nUpdating Polly's name to 'Larry:'")
conn.execute("UPDATE CONTACTS set NAME = 'Larry' where ID = 10")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, age, address from CONTACTS")
print("\nHere are all the records:")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("AGE = ", row[2])
   print("ADDRESS = ", row[3], "\n")
conn.close()

# Delete a record from the table.
conn = sqlite3.connect("test.db")
print("\nLet's remove Roger")
conn.execute("DELETE from CONTACTS where ID = 11;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)

print("\nHere are all the records:")
cursor = conn.execute("SELECT id, name, age, address from CONTACTS")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("AGE = ", row[2])
   print("ADDRESS = ", row[3], "\n")

print("Operations done successfully!")
conn.close()
