import compawdreDB as db


d = db.DB('compawdre.csv')

conn = d.get_connection()
select_all = "SELECT * FROM breed"
rows = conn.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)
