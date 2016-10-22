import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute('CREATE TABLE users (id INTEGER, firstName TEXT, age INTEGER)')
cur.execute('INSERT INTO users (id, firstName, age) VALUES(1, "Igor", 22)')
con.commit()
cur.execute('SELECT * FROM users')
print (cur.fetchall())
con.close()


