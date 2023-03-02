import sqlite3

conn = sqlite3.connect('hello_world.db')
c = conn.cursor()
c.execute('''CREATE TABLE test
       (id   INTEGER primary key autoincrement,
       data           TEXT    NOT NULL);''')

c.execute("INSERT INTO test (data) VALUES ('Hello world')")
conn.commit()
conn.close()

