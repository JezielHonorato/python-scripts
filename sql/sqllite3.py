import sqlite3

con = sqlite3.connect("database.db")

cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS filmes(fime TEXT, ano INTEGER, score INTEGER)
""")
con.commit() 

cur.execute("""
    INSERT INTO filmes VALUES
        ('Monty Python and the Holy Grail', 1975, 8),
        ('And Now for Something Completely Different', 1971, 7)
""")
con.commit() 

res = cur.execute("SELECT filme FROM filmes")

print(res.fetchall())

con.close()