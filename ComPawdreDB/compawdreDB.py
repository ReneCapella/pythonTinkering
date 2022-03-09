import sqlite3
import csv
import os.path

#EXAMPLE OF HOW TO USE THIS CLASS#
# import compawdreDB as db
#
#
# d = db.DB('compawdre.csv')
#
# conn = d.get_connection()
# select_all = "SELECT * FROM breed"
# rows = conn.execute(select_all).fetchall()
#
# # Output to the console screen
# for r in rows:
#     print(r)

class DB:
    def __init__(self, file):

        self.connection = None

        if not os.path.exists(file):
            raise Exception("File does not exist. Please enter a valid filename")

        with open(file, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

            a = data[0]
            b = ['id','name','image_url','hypoallergenic','breed_restriction','weight','energy','trainable','territorial','age']

            if not a == b:
                raise Exception('''Headers do not match.
                Headers should be
                id,name,image_url,hypoallergenic,breed_restriction,weight,energy,
                trainable,territorial,age''')
            elif len(data[1]) != 10:
                raise Exception("Innacurate number of columns for one or more records")


        file = open(file)

        contents = csv.reader(file)
        print("CSV loaded")

        conn = sqlite3.connect("compawdre.db")
        print("Database connected.")


        cursor = conn.cursor()

        # Create a table in the database.
        print("\nCreating a table in the ComPawdre database")
        cursor.execute('''CREATE TABLE breed
                 (ID            INT      PRIMARY KEY     NOT NULL,
                 NAME           TEXT                     NOT NULL,
                 IMAGE_URL      TEXT                     NOT NULL,
                 HYPOALLERGENIC BOOLEAN                  NOT NULL,
                 BREED_RESTRICTION BOOLEAN               NOT NULL,
                 WEIGHT         TEXT                     NOT NULL,
                 ENERGY         INT                      NOT NULL,
                 TRAINABLE      INT                      NOT NULL,
                 TERRITORIAL    INT                      NOT NULL,
                 AGE            TEXT                     NOT NULL);''')
        print("\nTable created.")

        insert_records = "INSERT INTO breed (ID,NAME,IMAGE_URL,HYPOALLERGENIC,BREED_RESTRICTION,WEIGHT,ENERGY,TRAINABLE,TERRITORIAL,AGE) \
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

        print("\nAdding some records to the table")
        cursor.executemany(insert_records, contents)

        select_all = "SELECT * FROM breed"
        rows = cursor.execute(select_all).fetchall()

        # Output to the console screen
        for r in rows:
            print(r)

        conn.commit()

        print("Operations done successfully!")
        conn.close()

    def get_connection(self):
        if not self.connection:
            self.connection = sqlite3.connect("compawdre.db")
        return self.connection
